from twisted.conch.ssh import common as common, sexpy as sexpy
from twisted.conch.ssh.common import int_from_bytes as int_from_bytes, int_to_bytes as int_to_bytes
from twisted.python import randbytes as randbytes
from twisted.python.compat import iterbytes as iterbytes, nativeString as nativeString
from twisted.python.constants import NamedConstant as NamedConstant, Names as Names
from typing import Any, Optional

class BadKeyError(Exception): ...
class EncryptedKeyError(Exception): ...
class BadFingerPrintFormat(Exception): ...

class FingerprintFormats(Names):
    MD5_HEX: Any = ...
    SHA256_BASE64: Any = ...

class PassphraseNormalizationError(Exception): ...

class Key:
    @classmethod
    def fromFile(cls, filename: Any, type: Optional[Any] = ..., passphrase: Optional[Any] = ...): ...
    @classmethod
    def fromString(cls, data: Any, type: Optional[Any] = ..., passphrase: Optional[Any] = ...): ...
    def __init__(self, keyObject: Any) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def isPublic(self): ...
    def public(self): ...
    def fingerprint(self, format: Any = ...): ...
    def type(self): ...
    def sshType(self): ...
    def size(self): ...
    def data(self): ...
    def blob(self): ...
    def privateBlob(self): ...
    def toString(self, type: Any, extra: Optional[Any] = ..., subtype: Optional[Any] = ..., comment: Optional[Any] = ..., passphrase: Optional[Any] = ...): ...
    def sign(self, data: Any): ...
    def verify(self, signature: Any, data: Any): ...
