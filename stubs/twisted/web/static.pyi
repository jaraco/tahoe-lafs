from twisted.internet import abstract as abstract, interfaces as interfaces
from twisted.python import components as components, filepath as filepath, log as log
from twisted.python.compat import nativeString as nativeString, networkString as networkString
from twisted.python.deprecate import deprecated as deprecated
from twisted.python.runtime import platformType as platformType
from twisted.python.url import URL as URL
from twisted.python.util import InsensitiveDict as InsensitiveDict
from twisted.web import http as http, resource as resource, server as server
from twisted.web.util import redirectTo as redirectTo
from typing import Any, Callable, Dict, Optional

dangerousPathError: Any

def isDangerous(path: Any): ...

class Data(resource.Resource):
    data: Any = ...
    type: Any = ...
    def __init__(self, data: Any, type: Any) -> None: ...
    def render_GET(self, request: Any): ...
    render_HEAD: Any = ...

def addSlash(request: Any): ...

class Redirect(resource.Resource):
    url: Any = ...
    def __init__(self, request: Any) -> None: ...
    def render(self, request: Any): ...

class Registry(components.Componentized):
    def __init__(self) -> None: ...
    def cachePath(self, path: Any, rsrc: Any) -> None: ...
    def getCachedPath(self, path: Any): ...

def loadMimeTypes(mimetype_locations: Optional[Any] = ..., init: Any = ...): ...
def getTypeAndEncoding(filename: Any, types: Any, encodings: Any, defaultType: Any): ...

class File(resource.Resource, filepath.FilePath):
    contentTypes: Any = ...
    contentEncodings: Any = ...
    processors: Dict[str, Callable[[str, Any], Data]] = ...
    indexNames: Any = ...
    type: Any = ...
    defaultType: Any = ...
    ignoredExts: Any = ...
    registry: Any = ...
    def __init__(self, path: Any, defaultType: str = ..., ignoredExts: Any = ..., registry: Optional[Any] = ..., allowExt: int = ...) -> None: ...
    def ignoreExt(self, ext: Any) -> None: ...
    childNotFound: Any = ...
    forbidden: Any = ...
    def directoryListing(self): ...
    def getChild(self, path: Any, request: Any): ...
    def openForReading(self): ...
    def getFileSize(self): ...
    def makeProducer(self, request: Any, fileForReading: Any): ...
    def render_GET(self, request: Any): ...
    render_HEAD: Any = ...
    def redirect(self, request: Any): ...
    def listNames(self): ...
    def listEntities(self): ...
    def createSimilarFile(self, path: Any): ...

class StaticProducer:
    bufferSize: Any = ...
    request: Any = ...
    fileObject: Any = ...
    def __init__(self, request: Any, fileObject: Any) -> None: ...
    def start(self) -> None: ...
    def resumeProducing(self) -> None: ...
    def stopProducing(self) -> None: ...

class NoRangeStaticProducer(StaticProducer):
    def start(self) -> None: ...
    def resumeProducing(self) -> None: ...

class SingleRangeStaticProducer(StaticProducer):
    offset: Any = ...
    size: Any = ...
    def __init__(self, request: Any, fileObject: Any, offset: Any, size: Any) -> None: ...
    bytesWritten: int = ...
    def start(self) -> None: ...
    def resumeProducing(self) -> None: ...

class MultipleRangeStaticProducer(StaticProducer):
    rangeInfo: Any = ...
    def __init__(self, request: Any, fileObject: Any, rangeInfo: Any) -> None: ...
    rangeIter: Any = ...
    def start(self) -> None: ...
    partBoundary: Any = ...
    def resumeProducing(self) -> None: ...

class ASISProcessor(resource.Resource):
    path: Any = ...
    registry: Any = ...
    def __init__(self, path: Any, registry: Optional[Any] = ...) -> None: ...
    def render(self, request: Any): ...

def formatFileSize(size: Any): ...

class DirectoryLister(resource.Resource):
    template: str = ...
    linePattern: str = ...
    contentTypes: Any = ...
    contentEncodings: Any = ...
    defaultType: Any = ...
    dirs: Any = ...
    path: Any = ...
    def __init__(self, pathname: Any, dirs: Optional[Any] = ..., contentTypes: Any = ..., contentEncodings: Any = ..., defaultType: str = ...) -> None: ...
    def render(self, request: Any): ...
