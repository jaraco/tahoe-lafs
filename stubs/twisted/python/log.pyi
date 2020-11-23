import abc
from abc import ABC, abstractmethod
from twisted.logger import LegacyLogObserverWrapper as LegacyLogObserverWrapper, LoggingFile as LoggingFile
from twisted.logger._global import LogBeginner as LogBeginner
from twisted.python import context as context, failure as failure, reflect as reflect, util as util
from twisted.python.threadable import synchronize as synchronize
from typing import Any, Dict, Optional
from zope.interface import Interface

EventDict = Dict[str, Any]

class ILogContext: ...

class ILogObserver(Interface):
    def __call__(eventDict: EventDict) -> None: ...

def callWithContext(ctx: Any, func: Any, *args: Any, **kw: Any): ...
def callWithLogger(logger: Any, func: Any, *args: Any, **kw: Any): ...
def err(_stuff: Optional[Any] = ..., _why: Optional[Any] = ..., **kw: Any) -> None: ...
deferr = err

class Logger:
    def logPrefix(self): ...

class LogPublisher:
    synchronized: Any = ...
    showwarning: Any = ...
    def __init__(self, observerPublisher: Optional[Any] = ..., publishPublisher: Optional[Any] = ..., logBeginner: Optional[Any] = ..., warningsModule: Any = ...) -> None: ...
    @property
    def observers(self): ...
    def addObserver(self, other: Any) -> None: ...
    def removeObserver(self, other: Any) -> None: ...
    def msg(self, *message: Any, **kw: Any) -> None: ...

theLogPublisher: Any

def addObserver(observer: Any) -> None: ...
def removeObserver(observer: Any) -> None: ...
def msg(*message: Any, **event: Any) -> None: ...
def showwarning() -> None: ...
def textFromEventDict(eventDict: EventDict) -> Optional[str]: ...

class _GlobalStartStopObserver(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def emit(self, eventDict: EventDict) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class FileLogObserver(_GlobalStartStopObserver):
    timeFormat: Optional[str] = ...
    write: Any = ...
    flush: Any = ...
    def __init__(self, f: Any) -> None: ...
    def getTimezoneOffset(self, when: Any): ...
    def formatTime(self, when: Any): ...
    def emit(self, eventDict: EventDict) -> None: ...

class PythonLoggingObserver(_GlobalStartStopObserver):
    def __init__(self, loggerName: str = ...) -> None: ...
    def emit(self, eventDict: EventDict) -> None: ...

class StdioOnnaStick:
    closed: int = ...
    softspace: int = ...
    mode: str = ...
    name: str = ...
    isError: Any = ...
    encoding: Any = ...
    buf: str = ...
    def __init__(self, isError: int = ..., encoding: Optional[Any] = ...) -> None: ...
    def close(self) -> None: ...
    def fileno(self): ...
    def flush(self) -> None: ...
    def read(self) -> None: ...
    readline: Any = ...
    readlines: Any = ...
    seek: Any = ...
    tell: Any = ...
    def write(self, data: Any) -> None: ...
    def writelines(self, lines: Any) -> None: ...

def startLogging(file: Any, *a: Any, **kw: Any): ...
def startLoggingWithObserver(observer: Any, setStdout: int = ...) -> None: ...

class NullFile:
    softspace: int = ...
    def read(self) -> None: ...
    def write(self, bytes: Any) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def discardLogs() -> None: ...

logfile: Any
logerr: Any

class DefaultObserver(_GlobalStartStopObserver):
    stderr: Any = ...
    def emit(self, eventDict: EventDict) -> None: ...

defaultObserver: Any
