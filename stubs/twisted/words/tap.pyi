from twisted import plugin as plugin
from twisted.application import strports as strports
from twisted.application.service import MultiService as MultiService
from twisted.cred import checkers as checkers, credentials as credentials, portal as portal, strcred as strcred
from twisted.python import usage as usage
from twisted.words import iwords as iwords, service as service
from typing import Any

class Options(usage.Options, strcred.AuthOptionMixin):
    supportedInterfaces: Any = ...
    optParameters: Any = ...
    compData: Any = ...
    interfacePlugins: Any = ...
    plg: Any = ...
    def __init__(self, *a: Any, **kw: Any) -> None: ...
    def opt_group(self, name: Any) -> None: ...
    def opt_passwd(self, filename: Any) -> None: ...

def makeService(config: Any): ...
