from ._buffer import LimitedHistoryLogObserver as LimitedHistoryLogObserver
from ._file import FileLogObserver as FileLogObserver
from ._filter import FilteringLogObserver as FilteringLogObserver, LogLevelFilterPredicate as LogLevelFilterPredicate
from ._format import eventAsText as eventAsText
from ._io import LoggingFile as LoggingFile
from ._levels import LogLevel as LogLevel
from ._logger import Logger as Logger
from ._observer import LogPublisher as LogPublisher
from twisted.python.compat import currentframe as currentframe
from twisted.python.reflect import qual as qual
from typing import Any, Optional

MORE_THAN_ONCE_WARNING: str

class LogBeginner:
    def __init__(self, publisher: Any, errorStream: Any, stdio: Any, warningsModule: Any, initialBufferSize: Optional[Any] = ...): ...
    def beginLoggingTo(self, observers: Any, discardBuffer: bool = ..., redirectStandardIO: bool = ...) -> None: ...
    def showwarning(self, message: Any, category: Any, filename: Any, lineno: Any, file: Optional[Any] = ..., line: Optional[Any] = ...) -> None: ...

globalLogPublisher: Any
globalLogBeginner: Any
