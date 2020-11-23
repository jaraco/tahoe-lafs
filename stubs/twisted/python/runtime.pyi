from typing import Any, Optional

def shortPythonVersion() -> str: ...

knownPlatforms: Any

class Platform:
    type: Optional[str] = ...
    seconds: Any = ...
    def __init__(self, name: Optional[str]=..., platform: Optional[str]=...) -> None: ...
    def isKnown(self) -> bool: ...
    def getType(self) -> Optional[str]: ...
    def isMacOSX(self) -> bool: ...
    def isWinNT(self) -> bool: ...
    def isWindows(self) -> bool: ...
    def isVista(self) -> bool: ...
    def isLinux(self) -> bool: ...
    def isDocker(self, _initCGroupLocation: str=...) -> bool: ...
    def supportsThreads(self) -> bool: ...
    def supportsINotify(self) -> bool: ...

platform: Any
platformType: Any
seconds: Any
