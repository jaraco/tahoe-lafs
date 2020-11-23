import base64
import os
from twisted.python.compat import cmp as cmp, comparable as comparable
from twisted.python.runtime import platform as platform
from twisted.python.util import FancyEqMixin as FancyEqMixin
from twisted.python.win32 import ERROR_DIRECTORY as ERROR_DIRECTORY, ERROR_FILE_NOT_FOUND as ERROR_FILE_NOT_FOUND, ERROR_INVALID_NAME as ERROR_INVALID_NAME, ERROR_PATH_NOT_FOUND as ERROR_PATH_NOT_FOUND, O_BINARY as O_BINARY
from typing import Any, IO, Optional, Union
from zope.interface import Interface

islink: Any
randomBytes = os.urandom
armor = base64.urlsafe_b64encode

class IFilePath(Interface):
    sep: Any = ...
    def child(name: Any) -> None: ...
    def open(mode: str = ...) -> None: ...
    def changed() -> None: ...
    def getsize() -> None: ...
    def getModificationTime() -> None: ...
    def getStatusChangeTime() -> None: ...
    def getAccessTime() -> None: ...
    def exists() -> None: ...
    def isdir() -> None: ...
    def isfile() -> None: ...
    def children() -> None: ...
    def basename() -> None: ...
    def parent() -> None: ...
    def sibling(name: Any) -> None: ...

class InsecurePath(Exception): ...
class LinkError(Exception): ...

class UnlistableError(OSError):
    originalException: Any = ...
    def __init__(self, originalException: OSError) -> None: ...

class AbstractFilePath:
    def getContent(self): ...
    def parents(self) -> None: ...
    def children(self): ...
    def walk(self, descend: Optional[Any] = ...) -> None: ...
    def sibling(self, path: Any): ...
    def descendant(self, segments: Any): ...
    def segmentsFrom(self, ancestor: Any): ...
    def __hash__(self) -> Any: ...
    def getmtime(self): ...
    def getatime(self): ...
    def getctime(self): ...

class RWX(FancyEqMixin):
    compareAttributes: Any = ...
    read: Any = ...
    write: Any = ...
    execute: Any = ...
    def __init__(self, readable: Any, writable: Any, executable: Any) -> None: ...
    def shorthand(self): ...

class Permissions(FancyEqMixin):
    compareAttributes: Any = ...
    def __init__(self, statModeInt: Any) -> None: ...
    def shorthand(self): ...

class FilePath(AbstractFilePath):
    path: Union[bytes, str] = ...
    alwaysCreate: Any = ...
    def __init__(self, path: Any, alwaysCreate: bool = ...) -> None: ...
    @property
    def sep(self): ...
    def asBytesMode(self, encoding: Optional[Any] = ...): ...
    def asTextMode(self, encoding: Optional[Any] = ...): ...
    def child(self, path: Any): ...
    def preauthChild(self, path: Any): ...
    def childSearchPreauth(self, *paths: Any): ...
    def siblingExtensionSearch(self, *exts: Any): ...
    def realpath(self): ...
    def siblingExtension(self, ext: Any): ...
    def linkTo(self, linkFilePath: Any) -> None: ...
    def open(self, mode: str=...) -> IO[bytes]: ...
    def restat(self, reraise: bool = ...) -> None: ...
    def changed(self) -> None: ...
    def chmod(self, mode: Any) -> None: ...
    def getsize(self): ...
    def getModificationTime(self): ...
    def getStatusChangeTime(self): ...
    def getAccessTime(self): ...
    def getInodeNumber(self): ...
    def getDevice(self): ...
    def getNumberOfHardLinks(self): ...
    def getUserID(self): ...
    def getGroupID(self): ...
    def getPermissions(self): ...
    def exists(self): ...
    def isdir(self): ...
    def isfile(self): ...
    def isBlockDevice(self): ...
    def isSocket(self): ...
    def islink(self): ...
    def isabs(self): ...
    def listdir(self): ...
    def splitext(self): ...
    def touch(self) -> None: ...
    def remove(self) -> None: ...
    def makedirs(self, ignoreExistingDirectory: bool = ...): ...
    def globChildren(self, pattern: Any): ...
    def basename(self): ...
    def dirname(self): ...
    def parent(self): ...
    def setContent(self, content: Any, ext: bytes = ...) -> None: ...
    def __cmp__(self, other: Any): ...
    def createDirectory(self) -> None: ...
    def requireCreate(self, val: int = ...) -> None: ...
    def create(self) -> IO[bytes]: ...
    def temporarySibling(self, extension: bytes = ...): ...
    def copyTo(self, destination: Any, followLinks: bool = ...) -> None: ...
    def moveTo(self, destination: Any, followLinks: bool = ...) -> None: ...
