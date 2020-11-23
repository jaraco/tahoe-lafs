from errno import WSAECONNREFUSED, WSAEINTR, WSAEMSGSIZE, WSAEWOULDBLOCK
from twisted.internet import abstract as abstract, address as address, base as base, defer as defer, error as error, interfaces as interfaces
from twisted.python import failure as failure, log as log
from twisted.python.runtime import platformType as platformType
from typing import Any, Optional

EMSGSIZE = WSAEMSGSIZE
ECONNREFUSED = WSAECONNREFUSED
EAGAIN = WSAEWOULDBLOCK
EINTR = WSAEINTR

class Port(base.BasePort):
    addressFamily: Any = ...
    socketType: Any = ...
    maxThroughput: Any = ...
    port: Any = ...
    protocol: Any = ...
    maxPacketSize: Any = ...
    interface: Any = ...
    def __init__(self, port: Any, proto: Any, interface: str = ..., maxPacketSize: int = ..., reactor: Optional[Any] = ...) -> None: ...
    def getHandle(self): ...
    def startListening(self) -> None: ...
    def doRead(self) -> None: ...
    def write(self, datagram: Any, addr: Optional[Any] = ...): ...
    def writeSequence(self, seq: Any, addr: Any) -> None: ...
    def connect(self, host: Any, port: Any) -> None: ...
    def stopListening(self): ...
    def loseConnection(self) -> None: ...
    def connectionLost(self, reason: Optional[Any] = ...) -> None: ...
    logstr: Any = ...
    def setLogStr(self) -> None: ...
    def logPrefix(self): ...
    def getHost(self): ...
    def setBroadcastAllowed(self, enabled: Any) -> None: ...
    def getBroadcastAllowed(self): ...

class MulticastMixin:
    def getOutgoingInterface(self): ...
    def setOutgoingInterface(self, addr: Any): ...
    def getLoopbackMode(self): ...
    def setLoopbackMode(self, mode: Any) -> None: ...
    def getTTL(self): ...
    def setTTL(self, ttl: Any) -> None: ...
    def joinGroup(self, addr: Any, interface: str = ...): ...
    def leaveGroup(self, addr: Any, interface: str = ...): ...

class MulticastPort(MulticastMixin, Port):
    listenMultiple: Any = ...
    def __init__(self, port: Any, proto: Any, interface: str = ..., maxPacketSize: int = ..., reactor: Optional[Any] = ..., listenMultiple: bool = ...) -> None: ...
    def createInternetSocket(self): ...
