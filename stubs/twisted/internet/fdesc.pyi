from typing import Any

def setNonBlocking(fd: Any) -> None: ...
def setBlocking(fd: Any) -> None: ...
def readFromFD(fd: Any, callback: Any): ...
def writeToFD(fd: Any, data: Any): ...
