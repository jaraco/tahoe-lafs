from twisted.internet import defer as defer
from twisted.internet.abstract import isIPAddress as isIPAddress
from twisted.names import common as common, dns as dns
from twisted.python import failure as failure
from twisted.python.compat import nativeString as nativeString
from twisted.python.filepath import FilePath as FilePath
from typing import Any, Optional

def searchFileForAll(hostsFile: Any, name: Any): ...
def searchFileFor(file: Any, name: Any): ...

class Resolver(common.ResolverBase):
    file: Any = ...
    ttl: Any = ...
    def __init__(self, file: bytes = ..., ttl: Any = ...) -> None: ...
    def lookupAddress(self, name: Any, timeout: Optional[Any] = ...): ...
    def lookupIPV6Address(self, name: Any, timeout: Optional[Any] = ...): ...
    lookupAllRecords: Any = ...
