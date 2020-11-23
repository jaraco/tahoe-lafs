from twisted import plugin as plugin
from twisted.cred.checkers import ICredentialsChecker as ICredentialsChecker
from twisted.cred.credentials import IUsernamePassword as IUsernamePassword
from twisted.cred.error import UnauthorizedLogin as UnauthorizedLogin
from twisted.cred.strcred import ICheckerFactory as ICheckerFactory
from twisted.internet import defer as defer
from twisted.python.compat import StringType as StringType
from typing import Any

def verifyCryptedPassword(crypted: Any, pw: Any): ...

class UNIXChecker:
    credentialInterfaces: Any = ...
    def checkPwd(self, pwd: Any, username: Any, password: Any): ...
    def checkSpwd(self, spwd: Any, username: Any, password: Any): ...
    def requestAvatarId(self, credentials: Any): ...

unixCheckerFactoryHelp: str

class UNIXCheckerFactory:
    authType: str = ...
    authHelp: Any = ...
    argStringFormat: str = ...
    credentialInterfaces: Any = ...
    def generateChecker(self, argstring: Any): ...

theUnixCheckerFactory: Any
