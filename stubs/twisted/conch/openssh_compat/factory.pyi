from twisted.conch.openssh_compat import primes as primes
from twisted.conch.ssh import common as common, factory as factory, keys as keys
from twisted.python.util import runAsEffectiveUser as runAsEffectiveUser

class OpenSSHFactory(factory.SSHFactory):
    dataRoot: str = ...
    moduliRoot: str = ...
    def getPublicKeys(self): ...
    def getPrivateKeys(self): ...
    def getPrimes(self): ...
