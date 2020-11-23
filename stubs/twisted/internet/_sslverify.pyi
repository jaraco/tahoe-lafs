from constantly import Flags, Names
from twisted.internet.abstract import isIPAddress as isIPAddress, isIPv6Address as isIPv6Address
from twisted.internet.defer import Deferred as Deferred
from twisted.internet.error import CertificateError as CertificateError, VerifyError as VerifyError
from twisted.internet.interfaces import IAcceptableCiphers as IAcceptableCiphers, ICipher as ICipher, IOpenSSLClientConnectionCreator as IOpenSSLClientConnectionCreator, IOpenSSLContextFactory as IOpenSSLContextFactory
from twisted.python import log as log, util as util
from twisted.python.compat import nativeString as nativeString, unicode as unicode
from twisted.python.deprecate import deprecated as deprecated
from twisted.python.failure import Failure as Failure
from twisted.python.randbytes import secureRandom as secureRandom
from twisted.python.util import FancyEqMixin as FancyEqMixin
from typing import Any, Optional
from zope.interface import Interface

class TLSVersion(Names):
    SSLv3: Any = ...
    TLSv1_0: Any = ...
    TLSv1_1: Any = ...
    TLSv1_2: Any = ...
    TLSv1_3: Any = ...

class SimpleVerificationError(Exception): ...

def simpleVerifyHostname(connection: Any, hostname: Any) -> None: ...
def simpleVerifyIPAddress(connection: Any, hostname: Any) -> None: ...

verifyHostname: Any
verifyIPAddress: Any
VerificationError: Any

class ProtocolNegotiationSupport(Flags):
    NPN: Any = ...
    ALPN: Any = ...

def protocolNegotiationMechanisms(): ...

class DistinguishedName(dict):
    def __init__(self, **kw: Any) -> None: ...
    def __getattr__(self, attr: Any): ...
    def __setattr__(self, attr: Any, value: Any) -> None: ...
    def inspect(self): ...
DN = DistinguishedName

class CertBase:
    original: Any = ...
    def __init__(self, original: Any) -> None: ...
    def getSubject(self): ...
    def __conform__(self, interface: Any): ...

class Certificate(CertBase):
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    @classmethod
    def load(Class: Any, requestData: Any, format: Any = ..., args: Any = ...): ...
    def dumpPEM(self): ...
    @classmethod
    def loadPEM(Class: Any, data: Any): ...
    @classmethod
    def peerFromTransport(Class: Any, transport: Any): ...
    @classmethod
    def hostFromTransport(Class: Any, transport: Any): ...
    def getPublicKey(self): ...
    def dump(self, format: Any = ...): ...
    def serialNumber(self): ...
    def digest(self, method: str = ...): ...
    def inspect(self): ...
    def getIssuer(self): ...
    def options(self, *authorities: Any) -> None: ...

class CertificateRequest(CertBase):
    @classmethod
    def load(Class: Any, requestData: Any, requestFormat: Any = ...): ...
    def dump(self, format: Any = ...): ...

class PrivateCertificate(Certificate):
    def newCertificate(self, newCertData: Any, format: Any = ...): ...
    @classmethod
    def load(Class: Any, data: Any, privateKey: Any, format: Any = ...): ...
    def inspect(self): ...
    def dumpPEM(self): ...
    @classmethod
    def loadPEM(Class: Any, data: Any): ...
    @classmethod
    def fromCertificateAndKeyPair(Class: Any, certificateInstance: Any, privateKey: Any): ...
    def options(self, *authorities: Any): ...
    def certificateRequest(self, format: Any = ..., digestAlgorithm: str = ...): ...
    def signCertificateRequest(self, requestData: Any, verifyDNCallback: Any, serialNumber: Any, requestFormat: Any = ..., certificateFormat: Any = ...): ...
    def signRequestObject(self, certificateRequest: Any, serialNumber: Any, secondsToExpiry: Any = ..., digestAlgorithm: str = ...): ...

class PublicKey:
    original: Any = ...
    def __init__(self, osslpkey: Any) -> None: ...
    def matches(self, otherKey: Any): ...
    def keyHash(self): ...
    def inspect(self): ...

class KeyPair(PublicKey):
    @classmethod
    def load(Class: Any, data: Any, format: Any = ...): ...
    def dump(self, format: Any = ...): ...
    def inspect(self): ...
    @classmethod
    def generate(Class: Any, kind: Any = ..., size: int = ...): ...
    def newCertificate(self, newCertData: Any, format: Any = ...): ...
    def requestObject(self, distinguishedName: Any, digestAlgorithm: str = ...): ...
    def certificateRequest(self, distinguishedName: Any, format: Any = ..., digestAlgorithm: str = ...): ...
    def signCertificateRequest(self, issuerDistinguishedName: Any, requestData: Any, verifyDNCallback: Any, serialNumber: Any, requestFormat: Any = ..., certificateFormat: Any = ..., secondsToExpiry: Any = ..., digestAlgorithm: str = ...): ...
    def signRequestObject(self, issuerDistinguishedName: Any, requestObject: Any, serialNumber: Any, secondsToExpiry: Any = ..., digestAlgorithm: str = ...): ...
    def selfSignedCert(self, serialNumber: Any, **kw: Any): ...

class IOpenSSLTrustRoot(Interface): ...

class OpenSSLCertificateAuthorities:
    def __init__(self, caCerts: Any) -> None: ...

def trustRootFromCertificates(certificates: Any): ...

class OpenSSLDefaultPaths: ...

def platformTrust(): ...

class ClientTLSOptions:
    def __init__(self, hostname: Any, ctx: Any) -> None: ...
    def clientConnectionForTLS(self, tlsProtocol: Any): ...

def optionsForClientTLS(hostname: Any, trustRoot: Optional[Any] = ..., clientCertificate: Optional[Any] = ..., acceptableProtocols: Optional[Any] = ..., **kw: Any): ...

class OpenSSLCertificateOptions:
    privateKey: Any = ...
    certificate: Any = ...
    method: Any = ...
    verify: Any = ...
    extraCertChain: Any = ...
    caCerts: Any = ...
    verifyDepth: Any = ...
    requireCertificate: Any = ...
    verifyOnce: Any = ...
    enableSingleUseKeys: Any = ...
    enableSessions: Any = ...
    fixBrokenPeers: Any = ...
    enableSessionTickets: Any = ...
    dhParameters: Any = ...
    trustRoot: Any = ...
    def __init__(self, privateKey: Optional[Any] = ..., certificate: Optional[Any] = ..., method: Optional[Any] = ..., verify: bool = ..., caCerts: Optional[Any] = ..., verifyDepth: int = ..., requireCertificate: bool = ..., verifyOnce: bool = ..., enableSingleUseKeys: bool = ..., enableSessions: bool = ..., fixBrokenPeers: bool = ..., enableSessionTickets: bool = ..., extraCertChain: Optional[Any] = ..., acceptableCiphers: Optional[Any] = ..., dhParameters: Optional[Any] = ..., trustRoot: Optional[Any] = ..., acceptableProtocols: Optional[Any] = ..., raiseMinimumTo: Optional[Any] = ..., insecurelyLowerMinimumTo: Optional[Any] = ..., lowerMaximumSecurityTo: Optional[Any] = ...) -> None: ...
    def getContext(self): ...

class OpenSSLCipher(FancyEqMixin):
    compareAttributes: Any = ...
    fullName: Any = ...
    def __init__(self, fullName: Any) -> None: ...

class OpenSSLAcceptableCiphers:
    def __init__(self, ciphers: Any) -> None: ...
    def selectCiphers(self, availableCiphers: Any): ...
    @classmethod
    def fromOpenSSLCipherString(cls, cipherString: Any): ...

defaultCiphers: Any

class _ChooseDiffieHellmanEllipticCurve:
    configureECDHCurve: Any = ...
    def __init__(self, openSSLVersion: Any, openSSLlib: Any, openSSLcrypto: Any) -> None: ...

class OpenSSLDiffieHellmanParameters:
    def __init__(self, parameters: Any) -> None: ...
    @classmethod
    def fromFile(cls, filePath: Any): ...
