import code
from twisted.conch import recvline as recvline
from twisted.internet import defer as defer
from twisted.python.htmlizer import TokenPrinter as TokenPrinter
from typing import Any, Optional

class FileWrapper:
    softspace: int = ...
    state: str = ...
    o: Any = ...
    def __init__(self, o: Any) -> None: ...
    def flush(self) -> None: ...
    def write(self, data: Any) -> None: ...
    def writelines(self, lines: Any) -> None: ...

class ManholeInterpreter(code.InteractiveInterpreter):
    numDeferreds: int = ...
    handler: Any = ...
    filename: Any = ...
    def __init__(self, handler: Any, locals: Optional[Any] = ..., filename: str = ...) -> None: ...
    buffer: Any = ...
    def resetBuffer(self) -> None: ...
    def push(self, line: Any): ...
    def runcode(self, *a: Any, **kw: Any) -> None: ...
    def displayhook(self, obj: Any) -> None: ...
    def write(self, data: Any, isAsync: Optional[Any] = ..., **kwargs: Any) -> None: ...

CTRL_C: bytes
CTRL_D: bytes
CTRL_BACKSLASH: bytes
CTRL_L: bytes
CTRL_A: bytes
CTRL_E: bytes

class Manhole(recvline.HistoricRecvLine):
    namespace: Any = ...
    def __init__(self, namespace: Optional[Any] = ...) -> None: ...
    interpreter: Any = ...
    def connectionMade(self) -> None: ...
    pn: int = ...
    lineBuffer: Any = ...
    lineBufferIndex: int = ...
    def handle_INT(self) -> None: ...
    def handle_EOF(self) -> None: ...
    def handle_FF(self) -> None: ...
    def handle_QUIT(self) -> None: ...
    def addOutput(self, data: Any, isAsync: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def lineReceived(self, line: Any) -> None: ...

class VT102Writer:
    typeToColor: Any = ...
    normalColor: bytes = ...
    written: Any = ...
    def __init__(self) -> None: ...
    def color(self, type: Any): ...
    def write(self, token: Any, type: Optional[Any] = ...) -> None: ...
    def __bytes__(self): ...

def lastColorizedLine(source: Any): ...

class ColoredManhole(Manhole):
    def getSource(self): ...
    def characterReceived(self, ch: Any, moreCharactersComing: Any) -> None: ...
