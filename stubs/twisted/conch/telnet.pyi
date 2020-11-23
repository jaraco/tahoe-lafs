from twisted.internet import interfaces as iinternet, protocol
from twisted.protocols import basic
from typing import Any, Optional

class ITelnetProtocol(iinternet.IProtocol):
    def unhandledCommand(command: Any, argument: Any) -> None: ...
    def unhandledSubnegotiation(command: Any, data: Any) -> None: ...
    def enableLocal(option: Any) -> None: ...
    def enableRemote(option: Any) -> None: ...
    def disableLocal(option: Any) -> None: ...
    def disableRemote(option: Any) -> None: ...

class ITelnetTransport(iinternet.ITransport):
    def do(option: Any) -> None: ...
    def dont(option: Any) -> None: ...
    def will(option: Any) -> None: ...
    def wont(option: Any) -> None: ...
    def requestNegotiation(about: Any, data: Any) -> None: ...

class TelnetError(Exception): ...
class NegotiationError(TelnetError): ...
class OptionRefused(NegotiationError): ...
class AlreadyEnabled(NegotiationError): ...
class AlreadyDisabled(NegotiationError): ...
class AlreadyNegotiating(NegotiationError): ...

class TelnetProtocol(protocol.Protocol):
    def unhandledCommand(self, command: Any, argument: Any) -> None: ...
    def unhandledSubnegotiation(self, command: Any, data: Any) -> None: ...
    def enableLocal(self, option: Any) -> None: ...
    def enableRemote(self, option: Any) -> None: ...
    def disableLocal(self, option: Any) -> None: ...
    def disableRemote(self, option: Any) -> None: ...

class Telnet(protocol.Protocol):
    state: str = ...
    options: Any = ...
    negotiationMap: Any = ...
    commandMap: Any = ...
    def __init__(self) -> None: ...
    class _OptionState:
        class _Perspective:
            state: str = ...
            negotiating: bool = ...
            onResult: Any = ...
        us: Any = ...
        him: Any = ...
        def __init__(self) -> None: ...
    def getOptionState(self, opt: Any): ...
    def will(self, option: Any): ...
    def wont(self, option: Any): ...
    def do(self, option: Any): ...
    def dont(self, option: Any): ...
    def requestNegotiation(self, about: Any, data: Any) -> None: ...
    commands: Any = ...
    command: Any = ...
    def dataReceived(self, data: Any) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    def applicationDataReceived(self, data: Any) -> None: ...
    def unhandledCommand(self, command: Any, argument: Any) -> None: ...
    def commandReceived(self, command: Any, argument: Any) -> None: ...
    def unhandledSubnegotiation(self, command: Any, data: Any) -> None: ...
    def negotiate(self, data: Any) -> None: ...
    def telnet_WILL(self, option: Any) -> None: ...
    def will_no_false(self, state: Any, option: Any) -> None: ...
    def will_no_true(self, state: Any, option: Any) -> None: ...
    def will_yes_false(self, state: Any, option: Any) -> None: ...
    def will_yes_true(self, state: Any, option: Any) -> None: ...
    willMap: Any = ...
    def telnet_WONT(self, option: Any) -> None: ...
    def wont_no_false(self, state: Any, option: Any) -> None: ...
    def wont_no_true(self, state: Any, option: Any) -> None: ...
    def wont_yes_false(self, state: Any, option: Any) -> None: ...
    def wont_yes_true(self, state: Any, option: Any) -> None: ...
    wontMap: Any = ...
    def telnet_DO(self, option: Any) -> None: ...
    def do_no_false(self, state: Any, option: Any) -> None: ...
    def do_no_true(self, state: Any, option: Any) -> None: ...
    def do_yes_false(self, state: Any, option: Any) -> None: ...
    def do_yes_true(self, state: Any, option: Any) -> None: ...
    doMap: Any = ...
    def telnet_DONT(self, option: Any) -> None: ...
    def dont_no_false(self, state: Any, option: Any) -> None: ...
    def dont_no_true(self, state: Any, option: Any) -> None: ...
    def dont_yes_false(self, state: Any, option: Any) -> None: ...
    def dont_yes_true(self, state: Any, option: Any) -> None: ...
    dontMap: Any = ...
    def enableLocal(self, option: Any): ...
    def enableRemote(self, option: Any): ...
    def disableLocal(self, option: Any) -> None: ...
    def disableRemote(self, option: Any) -> None: ...

class ProtocolTransportMixin:
    def write(self, data: Any) -> None: ...
    def writeSequence(self, seq: Any) -> None: ...
    def loseConnection(self) -> None: ...
    def getHost(self): ...
    def getPeer(self): ...

class TelnetTransport(Telnet, ProtocolTransportMixin):
    disconnecting: bool = ...
    protocolFactory: Any = ...
    protocol: Any = ...
    protocolArgs: Any = ...
    protocolKwArgs: Any = ...
    def __init__(self, protocolFactory: Optional[Any] = ..., *a: Any, **kw: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    def enableLocal(self, option: Any): ...
    def enableRemote(self, option: Any): ...
    def disableLocal(self, option: Any): ...
    def disableRemote(self, option: Any): ...
    def unhandledSubnegotiation(self, command: Any, data: Any) -> None: ...
    def unhandledCommand(self, command: Any, argument: Any) -> None: ...
    def applicationDataReceived(self, data: Any) -> None: ...
    def write(self, data: Any) -> None: ...

class TelnetBootstrapProtocol(TelnetProtocol, ProtocolTransportMixin):
    protocol: Any = ...
    protocolFactory: Any = ...
    protocolArgs: Any = ...
    protocolKwArgs: Any = ...
    def __init__(self, protocolFactory: Any, *args: Any, **kw: Any) -> None: ...
    def connectionMade(self): ...
    def connectionLost(self, reason: Any) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def enableLocal(self, opt: Any): ...
    def enableRemote(self, opt: Any): ...
    def telnet_NAWS(self, data: Any) -> None: ...
    linemodeSubcommands: Any = ...
    def telnet_LINEMODE(self, data: Any) -> None: ...
    def linemode_SLC(self, data: Any) -> None: ...

class StatefulTelnetProtocol(basic.LineReceiver, TelnetProtocol):
    delimiter: bytes = ...
    state: str = ...
    def connectionLost(self, reason: Any) -> None: ...
    def lineReceived(self, line: Any) -> None: ...
    def telnet_Discard(self, line: Any) -> None: ...

class AuthenticatingTelnetProtocol(StatefulTelnetProtocol):
    state: str = ...
    protocol: Any = ...
    portal: Any = ...
    def __init__(self, portal: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    username: Any = ...
    def telnet_User(self, line: Any): ...
    def telnet_Password(self, line: Any): ...
