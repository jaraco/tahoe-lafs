from ._buffer import LimitedHistoryLogObserver as LimitedHistoryLogObserver
from ._file import FileLogObserver as FileLogObserver
from ._filter import FilteringLogObserver as FilteringLogObserver, LogLevelFilterPredicate as LogLevelFilterPredicate
from ._format import eventAsText as eventAsText
from ._interfaces import ILogObserver as ILogObserver
from ._io import LoggingFile as LoggingFile
from ._levels import LogLevel as LogLevel
from ._logger import Logger as Logger
from ._observer import LogPublisher as LogPublisher
from twisted.python.compat import currentframe as currentframe
from twisted.python.reflect import qual as qual
from typing import Any, IO, Iterable, Optional, Type

MORE_THAN_ONCE_WARNING: str

class LogBeginner:
    def __init__(self, publisher: LogPublisher, errorStream: IO[Any], stdio: object, warningsModule: Any, initialBufferSize: Optional[int]=...): ...
    def beginLoggingTo(self, observers: Iterable[ILogObserver], discardBuffer: bool=..., redirectStandardIO: bool=...) -> None: ...
    def showwarning(self, message: str, category: Type[Warning], filename: str, lineno: int, file: Optional[IO[Any]]=..., line: Optional[str]=...) -> None: ...

globalLogPublisher: Any
globalLogBeginner: Any
