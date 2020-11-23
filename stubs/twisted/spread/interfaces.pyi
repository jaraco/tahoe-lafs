from typing import Any
from zope.interface import Interface

class IJellyable(Interface):
    def jellyFor(jellier: Any) -> None: ...

class IUnjellyable(Interface):
    def unjellyFor(jellier: Any, jellyList: Any) -> None: ...
