from twisted.cred.credentials import ICredentials
from twisted.internet import protocol
from twisted.persisted import styles
from twisted.python import failure
from twisted.spread import banana
from twisted.spread.flavors import Cacheable as Cacheable, Copyable as Copyable, IPBRoot as IPBRoot, Jellyable as Jellyable, NoSuchMethod as NoSuchMethod, Referenceable as Referenceable, RemoteCache as RemoteCache, RemoteCacheObserver as RemoteCacheObserver, RemoteCopy as RemoteCopy, Root as Root, Serializable as Serializable, ViewPoint as ViewPoint, Viewable as Viewable, copyTags as copyTags, setCopierForClass as setCopierForClass, setCopierForClassTree as setCopierForClassTree, setFactoryForClass as setFactoryForClass, setUnjellyableFactoryForClass as setUnjellyableFactoryForClass, setUnjellyableForClass as setUnjellyableForClass, setUnjellyableForClassTree as setUnjellyableForClassTree
from typing import Any, Optional
from zope.interface import Interface

MAX_BROKER_REFS: int
portno: int

class ProtocolError(Exception): ...
class DeadReferenceError(ProtocolError): ...
class Error(Exception): ...

class RemoteError(Exception):
    remoteType: Any = ...
    remoteTraceback: Any = ...
    def __init__(self, remoteType: Any, value: Any, remoteTraceback: Any) -> None: ...

class RemoteMethod:
    obj: Any = ...
    name: Any = ...
    def __init__(self, obj: Any, name: Any) -> None: ...
    def __cmp__(self, other: Any): ...
    def __hash__(self) -> Any: ...
    def __call__(self, *args: Any, **kw: Any): ...

class PBConnectionLost(Exception): ...

class IPerspective(Interface):
    def perspectiveMessageReceived(broker: Any, message: Any, args: Any, kwargs: Any) -> None: ...

class Avatar:
    def perspectiveMessageReceived(self, broker: Any, message: Any, args: Any, kw: Any): ...

class AsReferenceable(Referenceable):
    remoteMessageReceived: Any = ...
    def __init__(self, object: Any, messageType: str = ...) -> None: ...

class RemoteReference(Serializable, styles.Ephemeral):
    luid: Any = ...
    broker: Any = ...
    doRefCount: Any = ...
    perspective: Any = ...
    disconnectCallbacks: Any = ...
    def __init__(self, perspective: Any, broker: Any, luid: Any, doRefCount: Any) -> None: ...
    def notifyOnDisconnect(self, callback: Any) -> None: ...
    def dontNotifyOnDisconnect(self, callback: Any) -> None: ...
    def jellyFor(self, jellier: Any): ...
    def unjellyFor(self, unjellier: Any, unjellyList: Any): ...
    def callRemote(self, _name: Any, *args: Any, **kw: Any): ...
    def remoteMethod(self, key: Any): ...
    def __cmp__(self, other: Any): ...
    def __hash__(self) -> Any: ...
    def __del__(self) -> None: ...

class Local:
    object: Any = ...
    perspective: Any = ...
    refcount: int = ...
    def __init__(self, object: Any, perspective: Optional[Any] = ...) -> None: ...
    def incref(self): ...
    def decref(self): ...

class CopyableFailure(failure.Failure, Copyable):
    unsafeTracebacks: int = ...
    def getStateToCopy(self): ...

class CopiedFailure(RemoteCopy, failure.Failure):
    def printTraceback(self, file: Optional[Any] = ..., elideFrameworkCode: int = ..., detail: str = ...) -> None: ...
    def throwExceptionIntoGenerator(self, g: Any): ...
    printBriefTraceback: Any = ...
    printDetailedTraceback: Any = ...

def failure2Copyable(fail: Any, unsafeTracebacks: int = ...): ...

class Broker(banana.Banana):
    version: int = ...
    username: Any = ...
    factory: Any = ...
    disconnected: int = ...
    disconnects: Any = ...
    failures: Any = ...
    connects: Any = ...
    localObjects: Any = ...
    security: Any = ...
    pageProducers: Any = ...
    currentRequestID: int = ...
    currentLocalID: int = ...
    unserializingPerspective: Any = ...
    luids: Any = ...
    remotelyCachedObjects: Any = ...
    remotelyCachedLUIDs: Any = ...
    locallyCachedObjects: Any = ...
    waitingForAnswers: Any = ...
    def __init__(self, isClient: int = ..., security: Any = ...) -> None: ...
    def resumeProducing(self) -> None: ...
    def pauseProducing(self) -> None: ...
    def stopProducing(self) -> None: ...
    def registerPageProducer(self, pager: Any) -> None: ...
    def expressionReceived(self, sexp: Any) -> None: ...
    def proto_version(self, vnum: Any) -> None: ...
    def sendCall(self, *exp: Any) -> None: ...
    def proto_didNotUnderstand(self, command: Any) -> None: ...
    def connectionReady(self) -> None: ...
    def connectionFailed(self) -> None: ...
    localSecurity: Any = ...
    remoteSecurity: Any = ...
    def connectionLost(self, reason: Any) -> None: ...
    def notifyOnDisconnect(self, notifier: Any) -> None: ...
    def notifyOnFail(self, notifier: Any) -> None: ...
    def notifyOnConnect(self, notifier: Any) -> None: ...
    def dontNotifyOnDisconnect(self, notifier: Any) -> None: ...
    def localObjectForID(self, luid: Any): ...
    maxBrokerRefsViolations: int = ...
    def registerReference(self, object: Any): ...
    def setNameForLocal(self, name: Any, object: Any) -> None: ...
    def remoteForName(self, name: Any): ...
    def cachedRemotelyAs(self, instance: Any, incref: int = ...): ...
    def remotelyCachedForLUID(self, luid: Any): ...
    def cacheRemotely(self, instance: Any): ...
    def cacheLocally(self, cid: Any, instance: Any) -> None: ...
    def cachedLocallyAs(self, cid: Any): ...
    serializingPerspective: Any = ...
    jellyMethod: Any = ...
    jellyArgs: Any = ...
    jellyKw: Any = ...
    def serialize(self, object: Any, perspective: Optional[Any] = ..., method: Optional[Any] = ..., args: Optional[Any] = ..., kw: Optional[Any] = ...): ...
    def unserialize(self, sexp: Any, perspective: Optional[Any] = ...): ...
    def newLocalID(self): ...
    def newRequestID(self): ...
    def proto_message(self, requestID: Any, objectID: Any, message: Any, answerRequired: Any, netArgs: Any, netKw: Any) -> None: ...
    def proto_cachemessage(self, requestID: Any, objectID: Any, message: Any, answerRequired: Any, netArgs: Any, netKw: Any) -> None: ...
    def proto_answer(self, requestID: Any, netResult: Any) -> None: ...
    def proto_error(self, requestID: Any, fail: Any) -> None: ...
    def sendDecRef(self, objectID: Any) -> None: ...
    def proto_decref(self, objectID: Any) -> None: ...
    def decCacheRef(self, objectID: Any) -> None: ...
    def proto_decache(self, objectID: Any) -> None: ...
    def proto_uncache(self, objectID: Any) -> None: ...

def respond(challenge: Any, password: Any): ...
def challenge(): ...

class PBClientFactory(protocol.ClientFactory):
    protocol: Any = ...
    unsafeTracebacks: bool = ...
    security: Any = ...
    def __init__(self, unsafeTracebacks: bool = ..., security: Any = ...) -> None: ...
    def buildProtocol(self, addr: Any): ...
    def clientConnectionFailed(self, connector: Any, reason: Any) -> None: ...
    def clientConnectionLost(self, connector: Any, reason: Any, reconnecting: int = ...) -> None: ...
    rootObjectRequests: Any = ...
    def clientConnectionMade(self, broker: Any) -> None: ...
    def getRootObject(self): ...
    def disconnect(self) -> None: ...
    def login(self, credentials: Any, client: Optional[Any] = ...): ...

class PBServerFactory(protocol.ServerFactory):
    unsafeTracebacks: bool = ...
    protocol: Any = ...
    root: Any = ...
    security: Any = ...
    def __init__(self, root: Any, unsafeTracebacks: bool = ..., security: Any = ...) -> None: ...
    def buildProtocol(self, addr: Any): ...
    def clientConnectionMade(self, protocol: Any) -> None: ...

class IUsernameMD5Password(ICredentials):
    def checkPassword(password: Any) -> None: ...
    def checkMD5Password(password: Any) -> None: ...

class _PortalRoot:
    portal: Any = ...
    def __init__(self, portal: Any) -> None: ...
    def rootObject(self, broker: Any): ...

class _JellyableAvatarMixin: ...

class _PortalWrapper(Referenceable, _JellyableAvatarMixin):
    portal: Any = ...
    broker: Any = ...
    def __init__(self, portal: Any, broker: Any) -> None: ...
    def remote_login(self, username: Any): ...
    def remote_loginAnonymous(self, mind: Any): ...

class _PortalAuthChallenger(Referenceable, _JellyableAvatarMixin):
    portal: Any = ...
    broker: Any = ...
    username: Any = ...
    challenge: Any = ...
    def __init__(self, portal: Any, broker: Any, username: Any, challenge: Any) -> None: ...
    response: Any = ...
    def remote_respond(self, response: Any, mind: Any): ...
    def checkPassword(self, password: Any): ...
    def checkMD5Password(self, md5Password: Any): ...
