from twisted.internet import protocol as protocol
from twisted.persisted import styles as styles
from twisted.python import log as log
from twisted.python.compat import iterbytes as iterbytes, long as long
from twisted.python.reflect import fullyQualifiedName as fullyQualifiedName
from typing import Any

class BananaError(Exception): ...

def int2b128(integer: Any, stream: Any) -> None: ...
def b1282int(st: Any): ...

LIST: Any
INT: Any
STRING: Any
NEG: Any
FLOAT: Any
LONGINT: Any
LONGNEG: Any
VOCAB: Any
HIGH_BIT_SET: Any

def setPrefixLimit(limit: Any) -> None: ...

SIZE_LIMIT: Any

class Banana(protocol.Protocol, styles.Ephemeral):
    knownDialects: Any = ...
    prefixLimit: Any = ...
    sizeLimit: Any = ...
    def setPrefixLimit(self, limit: Any) -> None: ...
    def connectionReady(self) -> None: ...
    def callExpressionReceived(self, obj: Any) -> None: ...
    currentDialect: Any = ...
    def connectionMade(self) -> None: ...
    def gotItem(self, item: Any) -> None: ...
    buffer: bytes = ...
    def dataReceived(self, chunk: Any) -> None: ...
    def expressionReceived(self, lst: Any) -> None: ...
    outgoingVocabulary: Any = ...
    incomingVocabulary: Any = ...
    listStack: Any = ...
    outgoingSymbols: Any = ...
    outgoingSymbolCount: int = ...
    isClient: Any = ...
    def __init__(self, isClient: int = ...) -> None: ...
    def sendEncoded(self, obj: Any) -> None: ...

def encode(lst: Any): ...
def decode(st: Any): ...
