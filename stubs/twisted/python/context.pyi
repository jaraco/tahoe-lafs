from typing import Any, Dict, Optional, Type

defaultContextDict: Dict[Type[object], Dict[str, str]]
setDefault: Any

class ContextTracker:
    contexts: Any = ...
    def __init__(self) -> None: ...
    def callWithContext(self, newContext: Any, func: Any, *args: Any, **kw: Any): ...
    def getContext(self, key: Any, default: Optional[Any] = ...): ...

class ThreadedContextTracker:
    storage: Any = ...
    def __init__(self) -> None: ...
    def currentContext(self): ...
    def callWithContext(self, ctx: Any, func: Any, *args: Any, **kw: Any): ...
    def getContext(self, key: Any, default: Optional[Any] = ...): ...

theContextTracker: Any
call: Any
get: Any

def installContextTracker(ctr: Any) -> None: ...
