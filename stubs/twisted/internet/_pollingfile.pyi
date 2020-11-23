from twisted.internet.interfaces import IConsumer as IConsumer, IPushProducer as IPushProducer
from twisted.python.compat import unicode as unicode
from typing import Any

MIN_TIMEOUT: float
MAX_TIMEOUT: float

class _PollableResource:
    active: bool = ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...

class _PollingTimer:
    reactor: Any = ...
    def __init__(self, reactor: Any) -> None: ...

class _PollableReadPipe(_PollableResource):
    pipe: Any = ...
    receivedCallback: Any = ...
    lostCallback: Any = ...
    def __init__(self, pipe: Any, receivedCallback: Any, lostCallback: Any) -> None: ...
    def checkWork(self): ...
    def cleanup(self) -> None: ...
    def close(self) -> None: ...
    def stopProducing(self) -> None: ...
    def pauseProducing(self) -> None: ...
    def resumeProducing(self) -> None: ...

FULL_BUFFER_SIZE: Any

class _PollableWritePipe(_PollableResource):
    disconnecting: bool = ...
    producer: Any = ...
    producerPaused: bool = ...
    streamingProducer: int = ...
    outQueue: Any = ...
    writePipe: Any = ...
    lostCallback: Any = ...
    def __init__(self, writePipe: Any, lostCallback: Any) -> None: ...
    def close(self) -> None: ...
    def bufferFull(self) -> None: ...
    def bufferEmpty(self): ...
    def registerProducer(self, producer: Any, streaming: Any) -> None: ...
    def unregisterProducer(self) -> None: ...
    def writeConnectionLost(self) -> None: ...
    def writeSequence(self, seq: Any) -> None: ...
    def write(self, data: Any) -> None: ...
    def checkWork(self): ...
