from twisted.cred.error import UnauthorizedLogin as UnauthorizedLogin
from typing import Any, Optional

class ConchError(Exception):
    value: Any = ...
    data: Any = ...
    def __init__(self, value: Any, data: Optional[Any] = ...) -> None: ...

class NotEnoughAuthentication(Exception): ...
class ValidPublicKey(UnauthorizedLogin): ...
class IgnoreAuthentication(Exception): ...
class MissingKeyStoreError(Exception): ...
class UserRejectedKey(Exception): ...
class InvalidEntry(Exception): ...

class HostKeyChanged(Exception):
    offendingEntry: Any = ...
    path: Any = ...
    lineno: Any = ...
    def __init__(self, offendingEntry: Any, path: Any, lineno: Any) -> None: ...
