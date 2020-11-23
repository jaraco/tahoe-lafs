from twisted.conch.ssh import agent as agent, channel as channel, keys as keys
from twisted.internet import protocol as protocol, reactor as reactor
from twisted.logger import Logger as Logger
from typing import Any

class SSHAgentClient(agent.SSHAgentClient):
    blobs: Any = ...
    def __init__(self) -> None: ...
    def getPublicKeys(self): ...
    def getPublicKey(self): ...

class SSHAgentForwardingChannel(channel.SSHChannel):
    buf: str = ...
    def channelOpen(self, specificData: Any): ...
    def dataReceived(self, data: Any) -> None: ...
    local: Any = ...
    def closed(self) -> None: ...

class SSHAgentForwardingLocal(protocol.Protocol): ...
