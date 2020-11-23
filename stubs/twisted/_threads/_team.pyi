from . import IWorker as IWorker
from ._convenience import Quit as Quit
from typing import Any, Optional

class Statistics:
    idleWorkerCount: Any = ...
    busyWorkerCount: Any = ...
    backloggedWorkCount: Any = ...
    def __init__(self, idleWorkerCount: Any, busyWorkerCount: Any, backloggedWorkCount: Any) -> None: ...

class Team:
    def __init__(self, coordinator: Any, createWorker: Any, logException: Any) -> None: ...
    def statistics(self): ...
    def grow(self, n: Any) -> None: ...
    def shrink(self, n: Optional[Any] = ...): ...
    def do(self, task: Any): ...
    def quit(self) -> None: ...
