from twisted.application import strports as strports
from twisted.protocols import portforward as portforward
from twisted.python import usage as usage
from typing import Any

class Options(usage.Options):
    synopsis: str = ...
    longdesc: str = ...
    optParameters: Any = ...
    compData: Any = ...

def makeService(config: Any): ...
