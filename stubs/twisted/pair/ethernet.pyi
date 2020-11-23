from twisted.internet import protocol as protocol
from twisted.pair import raw as raw
from typing import Any
from zope.interface import Interface

class IEthernetProtocol(Interface):
    def addProto(num: Any, proto: Any) -> None: ...
    def datagramReceived(data: Any, partial: Any) -> None: ...

class EthernetHeader:
    def __init__(self, data: Any) -> None: ...

class EthernetProtocol(protocol.AbstractDatagramProtocol):
    etherProtos: Any = ...
    def __init__(self) -> None: ...
    def addProto(self, num: Any, proto: Any) -> None: ...
    def datagramReceived(self, data: Any, partial: int = ...) -> None: ...
