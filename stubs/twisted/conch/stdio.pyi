from twisted.conch.insults.insults import ServerProtocol as ServerProtocol
from twisted.conch.manhole import ColoredManhole as ColoredManhole
from twisted.internet import defer as defer, protocol as protocol, reactor as reactor, stdio as stdio
from twisted.python import failure as failure, log as log, reflect as reflect
from typing import Any, Optional

class UnexpectedOutputError(Exception): ...

class TerminalProcessProtocol(protocol.ProcessProtocol):
    proto: Any = ...
    onConnection: Any = ...
    def __init__(self, proto: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def write(self, data: Any) -> None: ...
    def outReceived(self, data: Any) -> None: ...
    def errReceived(self, data: Any) -> None: ...
    def childConnectionLost(self, childFD: Any) -> None: ...
    def processEnded(self, reason: Any) -> None: ...

class ConsoleManhole(ColoredManhole):
    def connectionLost(self, reason: Any) -> None: ...

def runWithProtocol(klass: Any) -> None: ...
def main(argv: Optional[Any] = ...) -> None: ...
