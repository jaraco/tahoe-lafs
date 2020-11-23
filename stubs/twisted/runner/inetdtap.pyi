from twisted.application import internet as internet
from twisted.internet.protocol import ServerFactory as ServerFactory
from twisted.python import log as log, usage as usage
from twisted.runner import inetd as inetd, inetdconf as inetdconf
from typing import Any

protocolDict: Any

class Options(usage.Options):
    optParameters: Any = ...
    optFlags: Any = ...
    compData: Any = ...

def makeService(config: Any): ...
