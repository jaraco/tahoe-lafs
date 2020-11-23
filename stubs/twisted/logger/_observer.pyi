from ._interfaces import ILogObserver as ILogObserver, LogEvent as LogEvent
from ._logger import Logger as Logger
from twisted.python.failure import Failure as Failure
from typing import Any

OBSERVER_DISABLED: str

class LogPublisher:
    log: Any = ...
    def __init__(self, *observers: ILogObserver) -> None: ...
    def addObserver(self, observer: ILogObserver) -> None: ...
    def removeObserver(self, observer: ILogObserver) -> None: ...
    def __call__(self, event: LogEvent) -> None: ...

def bitbucketLogObserver(event: LogEvent) -> None: ...
