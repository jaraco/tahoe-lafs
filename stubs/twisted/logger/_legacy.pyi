from ._format import formatEvent as formatEvent
from ._interfaces import ILogObserver as ILogObserver, LogEvent as LogEvent
from ._levels import LogLevel as LogLevel
from ._stdlib import StringifiableFromEvent as StringifiableFromEvent, fromStdlibLogLevelMapping as fromStdlibLogLevelMapping
from twisted.python.log import ILogObserver as ILegacyLogObserver
from typing import Any, Callable, Dict, Optional

class LegacyLogObserverWrapper:
    legacyObserver: Any = ...
    def __init__(self, legacyObserver: ILegacyLogObserver) -> None: ...
    def __call__(self, event: LogEvent) -> None: ...

def publishToNewObserver(observer: ILogObserver, eventDict: Dict[str, Any], textFromEventDict: Callable[[Dict[str, Any]], Optional[str]]) -> None: ...
