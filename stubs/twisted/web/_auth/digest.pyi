from twisted.cred import credentials as credentials
from twisted.web.iweb import ICredentialFactory as ICredentialFactory
from typing import Any

class DigestCredentialFactory:
    scheme: bytes = ...
    digest: Any = ...
    def __init__(self, algorithm: Any, authenticationRealm: Any) -> None: ...
    def getChallenge(self, request: Any): ...
    def decode(self, response: Any, request: Any): ...
