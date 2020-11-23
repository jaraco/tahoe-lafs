from ._logger import Logger as Logger
from typing import Any, Dict
from zope.interface import Interface

LogEvent = Dict[str, Any]
LogTrace: Any

class ILogObserver(Interface):
    def __call__(event: LogEvent) -> None: ...
