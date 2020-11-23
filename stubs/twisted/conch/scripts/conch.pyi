from twisted.conch.client import connect as connect, default as default
from twisted.conch.client.options import ConchOptions as ConchOptions
from twisted.conch.error import ConchError as ConchError
from twisted.conch.ssh import channel as channel, common as common, connection as connection, forwarding as forwarding, session as session
from twisted.internet import reactor as reactor, stdio as stdio, task as task
from twisted.python import log as log, usage as usage
from twisted.python.compat import ioType as ioType, networkString as networkString
from typing import Any, List, Tuple

class ClientOptions(ConchOptions):
    synopsis: str = ...
    longdesc: str = ...
    optParameters: Any = ...
    optFlags: Any = ...
    compData: Any = ...
    localForwards: List[Tuple[int, Tuple[int, int]]] = ...
    remoteForwards: List[Tuple[int, Tuple[int, int]]] = ...
    def opt_escape(self, esc: Any) -> None: ...
    def opt_localforward(self, f: Any) -> None: ...
    def opt_remoteforward(self, f: Any) -> None: ...
    def parseArgs(self, host: Any, *command: Any) -> None: ...

options: Any
conn: Any
exitStatus: int
old: Any

def run(): ...
def handleError() -> None: ...
def doConnect() -> None: ...
def onConnect() -> None: ...
def reConnect() -> None: ...
def beforeShutdown() -> None: ...
def stopConnection() -> None: ...

class _KeepAlive:
    conn: Any = ...
    globalTimeout: Any = ...
    lc: Any = ...
    def __init__(self, conn: Any) -> None: ...
    def sendGlobal(self) -> None: ...

class SSHConnection(connection.SSHConnection):
    localForwards: Any = ...
    remoteForwards: Any = ...
    def serviceStarted(self) -> None: ...
    def serviceStopped(self) -> None: ...
    def requestRemoteForwarding(self, remotePort: Any, hostport: Any) -> None: ...
    def cancelRemoteForwarding(self, remotePort: Any) -> None: ...
    def channel_forwarded_tcpip(self, windowSize: Any, maxPacket: Any, data: Any): ...
    def channelClosed(self, channel: Any) -> None: ...

class SSHSession(channel.SSHChannel):
    name: bytes = ...
    escapeMode: int = ...
    stdio: Any = ...
    def channelOpen(self, foo: Any): ...
    def handleInput(self, char: Any) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def extReceived(self, t: Any, data: Any) -> None: ...
    def eofReceived(self) -> None: ...
    def closeReceived(self) -> None: ...
    def closed(self) -> None: ...
    def request_exit_status(self, data: Any) -> None: ...
    def sendEOF(self) -> None: ...
    def stopWriting(self) -> None: ...
    def startWriting(self) -> None: ...

class SSHListenClientForwardingChannel(forwarding.SSHListenClientForwardingChannel): ...
class SSHConnectForwardingChannel(forwarding.SSHConnectForwardingChannel): ...
