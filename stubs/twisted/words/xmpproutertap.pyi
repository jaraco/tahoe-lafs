from twisted.application import strports as strports
from twisted.python import usage as usage
from twisted.words.protocols.jabber import component as component
from typing import Any

class Options(usage.Options):
    optParameters: Any = ...
    optFlags: Any = ...

def makeService(config: Any): ...
