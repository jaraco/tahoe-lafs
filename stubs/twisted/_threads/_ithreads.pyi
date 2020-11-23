from typing import Any
from zope.interface import Interface

class AlreadyQuit(Exception): ...

class IWorker(Interface):
    def do(task: Any) -> None: ...
    def quit() -> None: ...

class IExclusiveWorker(IWorker): ...
