from twisted.internet import posixbase
from typing import Any

class ThreadedSelectReactor(posixbase.PosixReactorBase):
    reads: Any = ...
    writes: Any = ...
    toThreadQueue: Any = ...
    toMainThread: Any = ...
    workerThread: Any = ...
    mainWaker: Any = ...
    def __init__(self) -> None: ...
    def wakeUp(self) -> None: ...
    def callLater(self, *args: Any, **kw: Any): ...
    def ensureWorkerThread(self) -> None: ...
    def doThreadIteration(self, timeout: Any) -> None: ...
    doIteration: Any = ...
    def interleave(self, waker: Any, *args: Any, **kw: Any) -> None: ...
    def addReader(self, reader: Any) -> None: ...
    def addWriter(self, writer: Any) -> None: ...
    def removeReader(self, reader: Any) -> None: ...
    def removeWriter(self, writer: Any) -> None: ...
    def removeAll(self): ...
    def getReaders(self): ...
    def getWriters(self): ...
    def stop(self) -> None: ...
    def run(self, installSignalHandlers: bool = ...) -> None: ...
    def mainLoop(self) -> None: ...

def install(): ...
