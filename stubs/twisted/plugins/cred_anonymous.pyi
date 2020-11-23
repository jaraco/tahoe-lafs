from twisted import plugin as plugin
from twisted.cred.checkers import AllowAnonymousAccess as AllowAnonymousAccess
from twisted.cred.credentials import IAnonymous as IAnonymous
from twisted.cred.strcred import ICheckerFactory as ICheckerFactory
from typing import Any

anonymousCheckerFactoryHelp: str

class AnonymousCheckerFactory:
    authType: str = ...
    authHelp: Any = ...
    argStringFormat: str = ...
    credentialInterfaces: Any = ...
    def generateChecker(self, argstring: str = ...): ...

theAnonymousCheckerFactory: Any
