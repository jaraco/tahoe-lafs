from typing import Any, Optional

class Enum:
    group: Optional[str] = ...
    label: Any = ...
    def __init__(self, label: str) -> None: ...

class StatusEnum(Enum):
    group: str = ...

OFFLINE: Any
ONLINE: Any
AWAY: Any

class OfflineError(Exception): ...
