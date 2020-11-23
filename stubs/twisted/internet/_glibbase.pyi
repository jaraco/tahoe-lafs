from twisted.internet import base as base, posixbase as posixbase, selectreactor as selectreactor
from twisted.internet.interfaces import IReactorFDSet as IReactorFDSet
from twisted.python import log as log
from typing import Any

def ensureNotImported(moduleNames: Any, errorMessage: Any, preventImports: Any = ...) -> None: ...

class GlibWaker(posixbase._UnixWaker):
    def doRead(self) -> None: ...

class GlibReactorBase(posixbase.PosixReactorBase, posixbase._PollLikeMixin):
    context: Any = ...
    loop: Any = ...
    def __init__(self, glib_module: Any, gtk_module: Any, useGtk: bool = ...): ...
    def input_add(self, source: Any, condition: Any, callback: Any): ...
    def addReader(self, reader: Any) -> None: ...
    def addWriter(self, writer: Any) -> None: ...
    def getReaders(self): ...
    def getWriters(self): ...
    def removeAll(self): ...
    def removeReader(self, reader: Any) -> None: ...
    def removeWriter(self, writer: Any) -> None: ...
    def iterate(self, delay: int = ...) -> None: ...
    def crash(self) -> None: ...
    def stop(self) -> None: ...
    def run(self, installSignalHandlers: bool = ...) -> None: ...
    def callLater(self, *args: Any, **kwargs: Any): ...

class PortableGlibReactorBase(selectreactor.SelectReactor):
    loop: Any = ...
    def __init__(self, glib_module: Any, gtk_module: Any, useGtk: bool = ...): ...
    def crash(self) -> None: ...
    def run(self, installSignalHandlers: bool = ...) -> None: ...
    def simulate(self) -> None: ...
