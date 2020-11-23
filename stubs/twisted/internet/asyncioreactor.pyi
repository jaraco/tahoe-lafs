from asyncio import SelectorEventLoop
from twisted.internet.abstract import FileDescriptor as FileDescriptor
from twisted.internet.interfaces import IReactorFDSet as IReactorFDSet
from twisted.internet.posixbase import PosixReactorBase as PosixReactorBase
from twisted.logger import Logger as Logger
from twisted.python.log import callWithLogger as callWithLogger
from typing import Any, Optional

class AsyncioSelectorReactor(PosixReactorBase):
    def __init__(self, eventloop: Optional[SelectorEventLoop]=...) -> None: ...
    def addReader(self, reader: Any) -> None: ...
    def addWriter(self, writer: Any) -> None: ...
    def removeReader(self, reader: Any) -> None: ...
    def removeWriter(self, writer: Any) -> None: ...
    def removeAll(self): ...
    def getReaders(self): ...
    def getWriters(self): ...
    def iterate(self, timeout: Any) -> None: ...
    def run(self, installSignalHandlers: bool = ...) -> None: ...
    def stop(self) -> None: ...
    def crash(self) -> None: ...
    seconds: Any = ...
    def callLater(self, seconds: Any, f: Any, *args: Any, **kwargs: Any): ...
    def callFromThread(self, f: Any, *args: Any, **kwargs: Any): ...

def install(eventloop: Optional[Any] = ...) -> None: ...
