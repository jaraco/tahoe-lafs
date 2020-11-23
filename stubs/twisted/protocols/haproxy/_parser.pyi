from . import proxyEndpoint as proxyEndpoint
from twisted.internet.endpoints import IStreamServerEndpointStringParser as IStreamServerEndpointStringParser, quoteStringArgument as quoteStringArgument, serverFromString as serverFromString
from twisted.plugin import IPlugin as IPlugin
from typing import Any

def unparseEndpoint(args: Any, kwargs: Any): ...

class HAProxyServerParser:
    prefix: str = ...
    def parseStreamServer(self, reactor: Any, *args: Any, **kwargs: Any): ...
