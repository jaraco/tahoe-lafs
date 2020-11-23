from ._interfaces import ILogObserver as ILogObserver, LogEvent as LogEvent
from twisted.logger import globalLogPublisher as globalLogPublisher
from typing import Iterator, Sequence

def capturedLogs() -> Iterator[Sequence[LogEvent]]: ...
