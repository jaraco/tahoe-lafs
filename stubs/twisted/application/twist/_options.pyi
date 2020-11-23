from ..reactors import NoSuchReactor as NoSuchReactor, getReactorTypes as getReactorTypes, installReactor as installReactor
from ..runner._exit import ExitStatus as ExitStatus, exit as exit
from ..service import IServiceMaker as IServiceMaker
from twisted.copyright import version as version
from twisted.logger import InvalidLogLevelError as InvalidLogLevelError, LogLevel as LogLevel, jsonFileLogObserver as jsonFileLogObserver, textFileLogObserver as textFileLogObserver
from twisted.plugin import getPlugins as getPlugins
from twisted.python.usage import Options as Options, UsageError as UsageError
from typing import Any, Optional

openFile = open

class TwistOptions(Options):
    defaultReactorName: str = ...
    defaultLogLevel: Any = ...
    def __init__(self) -> None: ...
    def getSynopsis(self): ...
    def opt_version(self) -> None: ...
    def opt_reactor(self, name: Any) -> None: ...
    def installReactor(self, name: Any): ...
    def opt_log_level(self, levelName: Any) -> None: ...
    def opt_log_file(self, fileName: Any) -> None: ...
    def opt_log_format(self, format: Any) -> None: ...
    def selectDefaultLogObserver(self) -> None: ...
    def parseOptions(self, options: Optional[Any] = ...) -> None: ...
    @property
    def plugins(self): ...
    @property
    def subCommands(self): ...
    def postOptions(self) -> None: ...
