from twisted.internet.base import ReactorBase, _SignalReactorMixin
from twisted.python import log
from typing import Any, Optional

class _SocketWaker(log.Logger):
    disconnected: int = ...
    reactor: Any = ...
    r: Any = ...
    w: Any = ...
    fileno: Any = ...
    def __init__(self, reactor: Any) -> None: ...
    def wakeUp(self) -> None: ...
    def doRead(self) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...

class _FDWaker(log.Logger):
    disconnected: int = ...
    i: Any = ...
    o: Any = ...
    reactor: Any = ...
    fileno: Any = ...
    def __init__(self, reactor: Any): ...
    def doRead(self) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...

class _UnixWaker(_FDWaker):
    def wakeUp(self) -> None: ...

class _SIGCHLDWaker(_FDWaker):
    def __init__(self, reactor: Any) -> None: ...
    def install(self) -> None: ...
    def uninstall(self) -> None: ...
    def doRead(self) -> None: ...

class _DisconnectSelectableMixin: ...

class PosixReactorBase(_SignalReactorMixin, _DisconnectSelectableMixin, ReactorBase):
    waker: Any = ...
    def installWaker(self) -> None: ...
    def spawnProcess(self, processProtocol: Any, executable: Any, args: Any = ..., env: Any = ..., path: Optional[Any] = ..., uid: Optional[Any] = ..., gid: Optional[Any] = ..., usePTY: int = ..., childFDs: Optional[Any] = ...): ...
    def listenUDP(self, port: Any, protocol: Any, interface: str = ..., maxPacketSize: int = ...): ...
    def listenMulticast(self, port: Any, protocol: Any, interface: str = ..., maxPacketSize: int = ..., listenMultiple: bool = ...): ...
    def connectUNIX(self, address: Any, factory: Any, timeout: int = ..., checkPID: int = ...): ...
    def listenUNIX(self, address: Any, factory: Any, backlog: int = ..., mode: int = ..., wantPID: int = ...): ...
    def listenUNIXDatagram(self, address: Any, protocol: Any, maxPacketSize: int = ..., mode: int = ...): ...
    def connectUNIXDatagram(self, address: Any, protocol: Any, maxPacketSize: int = ..., mode: int = ..., bindAddress: Optional[Any] = ...): ...
    def adoptStreamPort(self, fileDescriptor: Any, addressFamily: Any, factory: Any): ...
    def adoptStreamConnection(self, fileDescriptor: Any, addressFamily: Any, factory: Any): ...
    def adoptDatagramPort(self, fileDescriptor: Any, addressFamily: Any, protocol: Any, maxPacketSize: int = ...): ...
    def listenTCP(self, port: Any, factory: Any, backlog: int = ..., interface: str = ...): ...
    def connectTCP(self, host: Any, port: Any, factory: Any, timeout: int = ..., bindAddress: Optional[Any] = ...): ...
    def connectSSL(self, host: Any, port: Any, factory: Any, contextFactory: Any, timeout: int = ..., bindAddress: Optional[Any] = ...): ...
    def listenSSL(self, port: Any, factory: Any, contextFactory: Any, backlog: int = ..., interface: str = ...): ...

class _PollLikeMixin: ...

class _ContinuousPolling(_PollLikeMixin, _DisconnectSelectableMixin):
    def __init__(self, reactor: Any) -> None: ...
    def iterate(self) -> None: ...
    def addReader(self, reader: Any) -> None: ...
    def addWriter(self, writer: Any) -> None: ...
    def removeReader(self, reader: Any) -> None: ...
    def removeWriter(self, writer: Any) -> None: ...
    def removeAll(self): ...
    def getReaders(self): ...
    def getWriters(self): ...
    def isReading(self, fd: Any): ...
    def isWriting(self, fd: Any): ...
