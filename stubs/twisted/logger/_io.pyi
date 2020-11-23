from ._levels import LogLevel as LogLevel
from typing import Any, Optional

class LoggingFile:
    softspace: int = ...
    level: Any = ...
    log: Any = ...
    def __init__(self, logger: Any, level: Any = ..., encoding: Optional[Any] = ...) -> None: ...
    @property
    def closed(self): ...
    @property
    def encoding(self): ...
    @property
    def mode(self): ...
    @property
    def newlines(self) -> None: ...
    @property
    def name(self): ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def fileno(self): ...
    def isatty(self): ...
    def write(self, string: Any) -> None: ...
    def writelines(self, lines: Any) -> None: ...
    read: Any = ...
    next: Any = ...
    readline: Any = ...
    readlines: Any = ...
    xreadlines: Any = ...
    seek: Any = ...
    tell: Any = ...
    truncate: Any = ...
