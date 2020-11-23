from twisted.conch.ssh import channel as channel, common as common
from twisted.internet import protocol as protocol, reactor as reactor
from twisted.internet.endpoints import HostnameEndpoint as HostnameEndpoint, connectProtocol as connectProtocol
from typing import Any

class SSHListenForwardingFactory(protocol.Factory):
    conn: Any = ...
    hostport: Any = ...
    klass: Any = ...
    def __init__(self, connection: Any, hostport: Any, klass: Any) -> None: ...
    def buildProtocol(self, addr: Any): ...

class SSHListenForwardingChannel(channel.SSHChannel):
    def channelOpen(self, specificData: Any) -> None: ...
    def openFailed(self, reason: Any) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def eofReceived(self) -> None: ...
    def closed(self) -> None: ...

class SSHListenClientForwardingChannel(SSHListenForwardingChannel):
    name: bytes = ...

class SSHListenServerForwardingChannel(SSHListenForwardingChannel):
    name: bytes = ...

class SSHConnectForwardingChannel(channel.SSHChannel):
    hostport: Any = ...
    client: Any = ...
    clientBuf: bytes = ...
    def __init__(self, hostport: Any, *args: Any, **kw: Any) -> None: ...
    def channelOpen(self, specificData: Any) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def closed(self) -> None: ...

def openConnectForwardingClient(remoteWindow: Any, remoteMaxPacket: Any, data: Any, avatar: Any): ...

class SSHForwardingClient(protocol.Protocol):
    channel: Any = ...
    buf: bytes = ...
    def __init__(self, channel: Any) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...

def packOpen_direct_tcpip(destination: Any, source: Any): ...
packOpen_forwarded_tcpip = packOpen_direct_tcpip

def unpackOpen_direct_tcpip(data: Any): ...
unpackOpen_forwarded_tcpip = unpackOpen_direct_tcpip

def packGlobal_tcpip_forward(peer: Any): ...
def unpackGlobal_tcpip_forward(data: Any): ...
