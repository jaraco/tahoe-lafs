import zope.interface
from typing import Any

class IProxyInfo(zope.interface.Interface):
    header: Any = ...
    source: Any = ...
    destination: Any = ...

class IProxyParser(zope.interface.Interface):
    def feed(self, data: Any) -> None: ...
    def parse(self, line: Any) -> None: ...
