from twisted.conch.ssh.transport import SSHCiphers as SSHCiphers, SSHClientTransport as SSHClientTransport
from twisted.python import usage as usage
from twisted.python.compat import unicode as unicode
from typing import Any

class ConchOptions(usage.Options):
    optParameters: Any = ...
    optFlags: Any = ...
    compData: Any = ...
    identitys: Any = ...
    conns: Any = ...
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def opt_identity(self, i: Any) -> None: ...
    def opt_ciphers(self, ciphers: Any) -> None: ...
    def opt_macs(self, macs: Any) -> None: ...
    def opt_host_key_algorithms(self, hkas: Any) -> None: ...
    def opt_user_authentications(self, uas: Any) -> None: ...
