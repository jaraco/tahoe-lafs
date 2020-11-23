from twisted.conch import avatar as avatar
from twisted.conch.insults import insults as insults
from twisted.conch.ssh import factory as factory, session as session
from twisted.python import components as components
from typing import Any, Dict, Optional

class _Glue:
    def __init__(self, **kw: Any) -> None: ...
    def __getattr__(self, name: Any) -> None: ...

class TerminalSessionTransport:
    proto: Any = ...
    avatar: Any = ...
    chainedProtocol: Any = ...
    def __init__(self, proto: Any, chainedProtocol: Any, avatar: Any, width: Any, height: Any): ...

class TerminalSession(components.Adapter):
    transportFactory: Any = ...
    chainedProtocolFactory: Any = ...
    def getPty(self, term: Any, windowSize: Any, attrs: Any) -> None: ...
    def openShell(self, proto: Any) -> None: ...
    def execCommand(self, proto: Any, cmd: Any) -> None: ...
    def windowChanged(self, newWindowSize: Any) -> None: ...
    def eofReceived(self) -> None: ...
    def closed(self) -> None: ...

class TerminalUser(avatar.ConchUser, components.Adapter):
    def __init__(self, original: Any, avatarId: Any) -> None: ...

class TerminalRealm:
    userFactory: Any = ...
    sessionFactory: Any = ...
    transportFactory: Any = ...
    chainedProtocolFactory: Any = ...
    def __init__(self, transportFactory: Optional[Any] = ...) -> None: ...
    def requestAvatar(self, avatarId: Any, mind: Any, *interfaces: Any): ...

class ConchFactory(factory.SSHFactory):
    publicKeys: Dict[bytes, bytes] = ...
    privateKeys: Dict[bytes, bytes] = ...
    portal: Any = ...
    def __init__(self, portal: Any) -> None: ...
