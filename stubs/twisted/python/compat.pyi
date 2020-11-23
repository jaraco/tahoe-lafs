import FIXME as cookielib
import urlparse as urllib_parse
from base64 import decodestring as _b64decodebytes, encodestring as _b64encodebytes
from cgi import escape as escape
from collections import Sequence as Sequence
from functools import reduce as reduce
from io import BytesIO as NativeStringIO, IOBase
from sys import intern as intern
from types import FileType as FileType, InstanceType as InstanceType
from typing import Any, Optional
from urllib import quote as urlquote, unquote as urlunquote

adict = dict
set = set
frozenset = frozenset
reduce = reduce

def execfile(filename: Any, globals: Any, locals: Optional[Any] = ...) -> None: ...
cmp = cmp

def comparable(klass: Any): ...
unicode = str
long = int
unicode = unicode
long = long

def nativeString(s: Any): ...
def reraise(exception: Any, traceback: Any) -> None: ...
def iterbytes(originalBytes: Any) -> None: ...
def intToBytes(i: Any): ...
def lazyByteSlice(object: Any, offset: int = ..., size: Optional[Any] = ...): ...
def networkString(s: Any): ...
lazyByteSlice = buffer
StringType = basestring
StringType = str
InstanceType = object
FileType = IOBase

def iteritems(d: Any): ...
def itervalues(d: Any): ...
def items(d: Any): ...
range = range
xrange = range
izip = zip
range = xrange
xrange = xrange

def bytesEnviron(): ...
intern = intern
unichr = chr
raw_input = input
unichr = unichr
raw_input = raw_input

# Names in __all__ with no definition:
#   OrderedDict
#   _bytesChr
#   _bytesRepr
#   _coercedUnicode
#   _get_async_param
#   _keys
#   _tokenize
