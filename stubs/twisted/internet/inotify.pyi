from twisted.internet.abstract import FileDescriptor
from typing import Any, Optional

IN_ACCESS: int
IN_MODIFY: int
IN_ATTRIB: int
IN_CLOSE_WRITE: int
IN_CLOSE_NOWRITE: int
IN_OPEN: int
IN_MOVED_FROM: int
IN_MOVED_TO: int
IN_CREATE: int
IN_DELETE: int
IN_DELETE_SELF: int
IN_MOVE_SELF: int
IN_UNMOUNT: int
IN_Q_OVERFLOW: int
IN_IGNORED: int
IN_ONLYDIR: int
IN_DONT_FOLLOW: int
IN_MASK_ADD: int
IN_ISDIR: int
IN_ONESHOT: int
IN_CLOSE: Any
IN_MOVED: Any
IN_CHANGED: Any
IN_WATCH_MASK: Any

def humanReadableMask(mask: Any): ...

class _Watch:
    path: Any = ...
    mask: Any = ...
    autoAdd: Any = ...
    callbacks: Any = ...
    def __init__(self, path: Any, mask: Any = ..., autoAdd: bool = ..., callbacks: Optional[Any] = ...) -> None: ...

class INotify(FileDescriptor):
    connected: int = ...
    def __init__(self, reactor: Optional[Any] = ...) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    def fileno(self): ...
    def doRead(self) -> None: ...
    def watch(self, path: Any, mask: Any = ..., autoAdd: bool = ..., callbacks: Optional[Any] = ..., recursive: bool = ...): ...
    def ignore(self, path: Any) -> None: ...
