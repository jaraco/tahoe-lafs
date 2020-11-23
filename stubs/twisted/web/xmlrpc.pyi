import xmlrpc.client as xmlrpclib
from twisted.internet import protocol
from twisted.web import http, resource
from typing import Any, Optional

Fault = xmlrpclib.Fault
Binary = xmlrpclib.Binary
Boolean: Any
DateTime = xmlrpclib.DateTime

class NoSuchFunction(Fault): ...

class Handler:
    resource: Any = ...
    result: Any = ...
    def __init__(self, resource: Any, *args: Any) -> None: ...
    def run(self, *args: Any) -> None: ...

class XMLRPC(resource.Resource):
    NOT_FOUND: int = ...
    FAILURE: int = ...
    isLeaf: int = ...
    separator: str = ...
    allowedMethods: Any = ...
    subHandlers: Any = ...
    allowNone: Any = ...
    useDateTime: Any = ...
    def __init__(self, allowNone: bool = ..., useDateTime: bool = ...) -> None: ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def putSubHandler(self, prefix: Any, handler: Any) -> None: ...
    def getSubHandler(self, prefix: Any): ...
    def getSubHandlerPrefixes(self): ...
    def render_POST(self, request: Any): ...
    def lookupProcedure(self, procedurePath: Any): ...
    def listProcedures(self): ...

class XMLRPCIntrospection(XMLRPC):
    def __init__(self, parent: Any) -> None: ...
    def xmlrpc_listMethods(self): ...
    def xmlrpc_methodHelp(self, method: Any): ...
    def xmlrpc_methodSignature(self, method: Any): ...

class QueryProtocol(http.HTTPClient):
    def connectionMade(self) -> None: ...
    def handleStatus(self, version: Any, status: Any, message: Any) -> None: ...
    def handleResponse(self, contents: Any) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...

class _QueryFactory(protocol.ClientFactory):
    deferred: Any = ...
    protocol: Any = ...
    payload: Any = ...
    useDateTime: Any = ...
    def __init__(self, path: Any, host: Any, method: Any, user: Optional[Any] = ..., password: Optional[Any] = ..., allowNone: bool = ..., args: Any = ..., canceller: Optional[Any] = ..., useDateTime: bool = ...) -> None: ...
    def parseResponse(self, contents: Any) -> None: ...
    def clientConnectionLost(self, _: Any, reason: Any) -> None: ...
    clientConnectionFailed: Any = ...
    def badStatus(self, status: Any, message: Any) -> None: ...

class Proxy:
    queryFactory: Any = ...
    user: Any = ...
    password: Any = ...
    host: Any = ...
    port: Any = ...
    path: Any = ...
    secure: Any = ...
    allowNone: Any = ...
    useDateTime: Any = ...
    connectTimeout: Any = ...
    def __init__(self, url: Any, user: Optional[Any] = ..., password: Optional[Any] = ..., allowNone: bool = ..., useDateTime: bool = ..., connectTimeout: float = ..., reactor: Any = ...) -> None: ...
    def callRemote(self, method: Any, *args: Any): ...
