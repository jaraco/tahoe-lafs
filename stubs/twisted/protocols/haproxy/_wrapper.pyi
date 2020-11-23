from ._exceptions import InvalidProxyHeader as InvalidProxyHeader
from ._v1parser import V1Parser as V1Parser
from ._v2parser import V2Parser as V2Parser
from twisted.internet import interfaces as interfaces
from twisted.protocols import policies as policies
from typing import Any

class HAProxyProtocolWrapper(policies.ProtocolWrapper):
    def __init__(self, factory: Any, wrappedProtocol: Any) -> None: ...
    def dataReceived(self, data: Any): ...
    def getPeer(self): ...
    def getHost(self): ...

class HAProxyWrappingFactory(policies.WrappingFactory):
    protocol: Any = ...
    def logPrefix(self): ...

def proxyEndpoint(wrappedEndpoint: Any): ...
