from twisted import cred as cred
from twisted.internet import defer as defer, protocol as protocol, reactor as reactor
from twisted.protocols import basic as basic
from twisted.python import log as log
from typing import Any, Dict, Optional
from zope.interface import Interface

PORT: int
shortHeaders: Any
longHeaders: Any
statusCodes: Any
specialCases: Any

def dashCapitalize(s: Any): ...
def unq(s: Any): ...

class Via:
    transport: Any = ...
    host: Any = ...
    port: Any = ...
    ttl: Any = ...
    hidden: Any = ...
    received: Any = ...
    rportValue: Any = ...
    rportRequested: bool = ...
    branch: Any = ...
    maddr: Any = ...
    otherParams: Any = ...
    def __init__(self, host: Any, port: Any = ..., transport: str = ..., ttl: Optional[Any] = ..., hidden: bool = ..., received: Optional[Any] = ..., rport: Any = ..., branch: Optional[Any] = ..., maddr: Optional[Any] = ..., **kw: Any) -> None: ...
    @property
    def rport(self): ...
    @rport.setter
    def rport(self, newRPort: Any) -> None: ...
    def toString(self): ...

def parseViaHeader(value: Any): ...

class URL:
    username: Any = ...
    host: Any = ...
    password: Any = ...
    port: Any = ...
    transport: Any = ...
    usertype: Any = ...
    method: Any = ...
    tag: Any = ...
    ttl: Any = ...
    maddr: Any = ...
    other: Any = ...
    headers: Any = ...
    def __init__(self, host: Any, username: Optional[Any] = ..., password: Optional[Any] = ..., port: Optional[Any] = ..., transport: Optional[Any] = ..., usertype: Optional[Any] = ..., method: Optional[Any] = ..., ttl: Optional[Any] = ..., maddr: Optional[Any] = ..., tag: Optional[Any] = ..., other: Optional[Any] = ..., headers: Optional[Any] = ...) -> None: ...
    def toString(self) -> str: ...

def parseURL(url: Any, host: Optional[Any] = ..., port: Optional[Any] = ...): ...
def cleanRequestURL(url: Any) -> None: ...
def parseAddress(address: Any, host: Optional[Any] = ..., port: Optional[Any] = ..., clean: int = ...): ...

class SIPError(Exception):
    code: Any = ...
    phrase: Any = ...
    def __init__(self, code: Any, phrase: Optional[Any] = ...) -> None: ...

class RegistrationError(SIPError): ...

class Message:
    length: Any = ...
    headers: Any = ...
    body: str = ...
    finished: int = ...
    def __init__(self) -> None: ...
    def addHeader(self, name: Any, value: Any) -> None: ...
    def bodyDataReceived(self, data: Any) -> None: ...
    def creationFinished(self) -> None: ...
    def toString(self): ...

class Request(Message):
    method: Any = ...
    uri: Any = ...
    def __init__(self, method: Any, uri: Any, version: str = ...) -> None: ...

class Response(Message):
    code: Any = ...
    phrase: Any = ...
    def __init__(self, code: Any, phrase: Optional[Any] = ..., version: str = ...) -> None: ...

class MessagesParser(basic.LineReceiver):
    version: str = ...
    acceptResponses: int = ...
    acceptRequests: int = ...
    state: str = ...
    debug: int = ...
    messageReceived: Any = ...
    def __init__(self, messageReceivedCallback: Any) -> None: ...
    length: Any = ...
    bodyReceived: int = ...
    message: Any = ...
    header: Any = ...
    def reset(self, remainingData: str = ...) -> None: ...
    def invalidMessage(self) -> None: ...
    def dataDone(self) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def handleFirstLine(self, line: Any) -> None: ...
    def lineLengthExceeded(self, line: Any) -> None: ...
    def lineReceived(self, line: Any) -> None: ...
    def messageDone(self, remainingData: str = ...) -> None: ...
    def rawDataReceived(self, data: Any) -> None: ...

class Base(protocol.DatagramProtocol):
    PORT: Any = ...
    debug: bool = ...
    messages: Any = ...
    parser: Any = ...
    def __init__(self) -> None: ...
    def addMessage(self, msg: Any) -> None: ...
    def datagramReceived(self, data: Any, addr: Any) -> None: ...
    def deliverResponse(self, responseMessage: Any) -> None: ...
    def responseFromRequest(self, code: Any, request: Any): ...
    def sendMessage(self, destURL: Any, message: Any) -> None: ...
    def handle_request(self, message: Any, addr: Any) -> None: ...
    def handle_response(self, message: Any, addr: Any) -> None: ...

class IContact(Interface): ...

class Registration:
    secondsToExpiry: Any = ...
    contactURL: Any = ...
    def __init__(self, secondsToExpiry: Any, contactURL: Any) -> None: ...

class IRegistry(Interface):
    def registerAddress(domainURL: Any, logicalURL: Any, physicalURL: Any) -> None: ...
    def unregisterAddress(domainURL: Any, logicalURL: Any, physicalURL: Any) -> None: ...
    def getRegistrationInfo(logicalURL: Any) -> None: ...

class ILocator(Interface):
    def getAddress(logicalURL: Any) -> None: ...

class Proxy(Base):
    PORT: Any = ...
    locator: Any = ...
    host: Any = ...
    port: Any = ...
    def __init__(self, host: Optional[Any] = ..., port: Any = ...) -> None: ...
    def getVia(self): ...
    def handle_request(self, message: Any, addr: Any): ...
    def handle_request_default(self, message: Any, sourcePeer: Any): ...
    def deliverResponse(self, responseMessage: Any) -> None: ...
    def responseFromRequest(self, code: Any, request: Any): ...
    def handle_response(self, message: Any, addr: Any) -> None: ...
    def gotResponse(self, message: Any, addr: Any) -> None: ...

class IAuthorizer(Interface):
    def getChallenge(peer: Any) -> None: ...
    def decode(response: Any) -> None: ...

class RegisterProxy(Proxy):
    portal: Any = ...
    registry: Any = ...
    authorizers: Dict[str, IAuthorizer] = ...
    liveChallenges: Any = ...
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def handle_ACK_request(self, message: Any, host_port: Any) -> None: ...
    def handle_REGISTER_request(self, message: Any, host_port: Any): ...
    def unauthorized(self, message: Any, host: Any, port: Any) -> None: ...
    def login(self, message: Any, host: Any, port: Any) -> None: ...
    def register(self, message: Any, host: Any, port: Any) -> None: ...
    def unregister(self, message: Any, toURL: Any, contact: Any) -> None: ...

class InMemoryRegistry:
    domain: Any = ...
    users: Any = ...
    def __init__(self, domain: Any) -> None: ...
    def getAddress(self, userURI: Any): ...
    def getRegistrationInfo(self, userURI: Any): ...
    def registerAddress(self, domainURL: Any, logicalURL: Any, physicalURL: Any): ...
    def unregisterAddress(self, domainURL: Any, logicalURL: Any, physicalURL: Any): ...
