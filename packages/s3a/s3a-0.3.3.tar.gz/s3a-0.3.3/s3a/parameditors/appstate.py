import typing as t
from pathlib import Path
from typing import List, Dict, Union, Callable, Any

import numpy as np
import pandas as pd
from pyqtgraph.parametertree import Parameter
from utilitys import ParamEditor, fns

from s3a import PRJ_SINGLETON
from s3a.constants import APP_STATE_DIR
from s3a.generalutils import safeCallFuncList, hierarchicalUpdate, safeCallFunc
from s3a.structures import FilePath
from utilitys.fns import serAsFrame, attemptFileLoad, raiseErrorLater, warnLater


class AppStateEditor(ParamEditor):

  def __init__(self, parent=None, paramList: List[Dict] = None,
               saveDir: FilePath = APP_STATE_DIR, fileType='param', name=None,
               topTreeChild: Parameter = None):
    # TODO: Add params to choose which features are saved, etc.
    super().__init__(parent, paramList, saveDir, fileType, name, topTreeChild)
    self._stateFuncsDf = pd.DataFrame(columns=['importFuncs', 'exportFuncs', 'required'])
    self.loading = False

    self.startupSettings = {}

  def saveParamValues(self, saveName: str=None, paramState: dict=None, **kwargs):
    if saveName is None:
      saveName = self.RECENT_STATE_FNAME
    if paramState is None:
      # TODO: May be good in the future to be able to choose which should be saved
      legitKeys = self._stateFuncsDf.index
      exportFuncs = self._stateFuncsDf.exportFuncs
      saveOnExitDir = self.saveDir/'saved_on_exit'
      saveOnExitDir.mkdir(exist_ok=True)
      rets, errs = safeCallFuncList(legitKeys, exportFuncs, [[saveOnExitDir]] * len(legitKeys))
      updateDict = {k: ret for k, ret in zip(legitKeys, rets) if ret is not None}
      paramState = dict(Parameters=paramState, **updateDict)
      for editor in PRJ_SINGLETON.quickLoader.listModel.uniqueEditors:
        if editor.stateName == 'Default':
          continue
        curSaveName = str(saveOnExitDir/editor.name)
        formattedName = editor.name.replace(' ', '').lower()
        editor.saveParamValues(curSaveName)
        paramState.update({formattedName: curSaveName})
    else:
      errs = []

    ret = super().saveParamValues(saveName, paramState, **kwargs)
    self.raiseErrMsgIfNeeded(errs)
    return ret

  def loadParamValues(self, stateName: Union[str, Path]=None, stateDict: dict = None, **kwargs):
    self.loading = True
    # Copy old settings to put them back after loading
    oldStartup = self.startupSettings.copy()
    try: # try block to ensure loading is false after
      if stateName is None:
        stateName = self.RECENT_STATE_FNAME
      if not stateName.exists() and stateDict is None:
        stateDict = {}
      if isinstance(stateDict, str):
        stateDict = {'quickloader': stateDict}
      stateDict = self._parseStateDict_includeRequired(stateName, stateDict)
      paramDict = stateDict.pop('Parameters', {}) or {}

      # It's possible for some functions (e.g. project load) to add or remove startup args,
      # so chack for this
      hierarchicalUpdate(self.startupSettings, kwargs)
      def nextKey():
        hierarchicalUpdate(stateDict, self.startupSettings)
        self.startupSettings.clear()
        legitKeys = self._stateFuncsDf.index.intersection(stateDict)
        if legitKeys.size > 0:
          return legitKeys[0]

      key = nextKey()
      rets, errs = [], {}
      while key:
        importFunc = self._stateFuncsDf.loc[key, 'importFuncs']
        arg = stateDict.pop(key, None)
        curRet, curErr = safeCallFunc(key, importFunc, arg)
        rets.append(curRet)
        if curErr: errs[key] = curErr
        key = nextKey()
      if errs:
        errPrint = [f'{k}: {v}' for (k, v) in errs.items()]
        warnLater('The following settings could not be loaded (shown as [setting]: [exception])\n'
             + "\n\n".join(errPrint), UserWarning)
      if stateDict:
        PRJ_SINGLETON.quickLoader.buildFromStartupParams(stateDict)
      ret = super().loadParamValues(stateName, paramDict)
    finally:
      self.loading = False
      hierarchicalUpdate(self.startupSettings, oldStartup)
    return ret

  def _parseStateDict_includeRequired(self, stateName: t.Union[str, Path], stateDict: dict = None):
    if self.RECENT_STATE_FNAME.exists():
      defaults = attemptFileLoad(self.RECENT_STATE_FNAME)
    else:
      defaults = {}
    try:
      out = self._parseStateDict(stateName, stateDict)
    except FileNotFoundError:
      out = {}
    for k in self._stateFuncsDf.index[self._stateFuncsDf['required']]:
      out.setdefault(k, defaults.get(k))
    return out

  @staticmethod
  def raiseErrMsgIfNeeded(errMsgs: List[str]):
    if len(errMsgs) > 0:
      err = IOError('Errors were encountered for the following parameters'
                         ' (shown as [parameter]: [exception])\n'
                       + "\n\n".join(errMsgs))
      fns.raiseErrorLater(err)


  def addImportExportOpts(self, optName: str, importFunc: Callable[[str], Any],
                          exportFunc: Callable[[Path], str], index:int=None,
                          required=False):
    """
    Main interface to the app state editor. By providing import and export functions,
    various aspects of the program state can be loaded and saved on demand.

    :param optName: What should this save option be called? E.g. when providing a
      load and save for annotation data, this is 'annotations'.
    :param importFunc: Function called when importing saved data. Takes in a
      full file path
    :param exportFunc: Function to save the app data. Input is a full folder path. Expects
      the output to be a full file path of the saved file. This file is then passed to
      'importFunc' on loading a param state
    :param index: Where to place this function. In most cases, this won't matter. However, some imports must be
      performed first / last otherwise app behavior may be undefined. In these cases, passing a value for index ensures
      correct placement of the import/export pair. By default, the function is added to the end of the import/export list.
    :param required: If *True*, this parameter is required every time param values are loaded.
      In the case it is missing from a load, the param editor first attempts to fetch this option
      from the most recent saved state.
    """
    newRow = pd.Series([importFunc, exportFunc, required], name=optName,
                       index=self._stateFuncsDf.columns)
    if index is not None:
      # First, shift old entries
      df = self._stateFuncsDf
      self._stateFuncsDf = pd.concat([df.iloc[:index], serAsFrame(newRow), df.iloc[index:]])
    else:
      self._stateFuncsDf: pd.DataFrame = self._stateFuncsDf.append(newRow)

  @property
  def RECENT_STATE_FNAME(self):
      return self.saveDir/f'recent.{self.fileType}'
