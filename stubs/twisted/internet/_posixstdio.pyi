from twisted.internet import error as error, interfaces as interfaces, process as process
from twisted.python import failure as failure, log as log
from typing import Any, Optional

class PipeAddress: ...

class StandardIO:
    disconnected: bool = ...
    disconnecting: bool = ...
    protocol: Any = ...
    def __init__(self, proto: Any, stdin: int = ..., stdout: int = ..., reactor: Optional[Any] = ...) -> None: ...
    def loseWriteConnection(self) -> None: ...
    def write(self, data: Any) -> None: ...
    def writeSequence(self, data: Any) -> None: ...
    def loseConnection(self) -> None: ...
    def getPeer(self): ...
    def getHost(self): ...
    def childDataReceived(self, fd: Any, data: Any) -> None: ...
    def childConnectionLost(self, fd: Any, reason: Any) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    def registerProducer(self, producer: Any, streaming: Any) -> None: ...
    def unregisterProducer(self) -> None: ...
    def stopProducing(self) -> None: ...
    def pauseProducing(self) -> None: ...
    def resumeProducing(self) -> None: ...
    def stopReading(self) -> None: ...
    def startReading(self) -> None: ...
