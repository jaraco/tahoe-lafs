from ._interfaces import LogEvent as LogEvent
from typing import Any, Optional

aFormatter: Any

class KeyFlattener:
    keys: Any = ...
    def __init__(self): ...
    def flatKey(self, fieldName: str, formatSpec: Optional[str], conversion: Optional[str]) -> str: ...

def flattenEvent(event: LogEvent) -> None: ...
def extractField(field: str, event: LogEvent) -> Any: ...
def flatFormat(event: LogEvent) -> str: ...
