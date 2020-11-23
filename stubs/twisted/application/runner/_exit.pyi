import typing
from enum import IntEnum
from typing import Any, Union

class Status:
    EX__BASE: int = ...
    EX_OK: int = ...
    EX_USAGE: Any = ...
    EX_DATAERR: Any = ...
    EX_NOINPUT: Any = ...
    EX_NOUSER: Any = ...
    EX_NOHOST: Any = ...
    EX_UNAVAILABLE: Any = ...
    EX_SOFTWARE: Any = ...
    EX_OSERR: Any = ...
    EX_OSFILE: Any = ...
    EX_CANTCREAT: Any = ...
    EX_IOERR: Any = ...
    EX_TEMPFAIL: Any = ...
    EX_PROTOCOL: Any = ...
    EX_NOPERM: Any = ...
    EX_CONFIG: Any = ...

class ExitStatus(IntEnum):
    EX_OK: Any = ...
    EX_USAGE: Any = ...
    EX_DATAERR: Any = ...
    EX_NOINPUT: Any = ...
    EX_NOUSER: Any = ...
    EX_NOHOST: Any = ...
    EX_UNAVAILABLE: Any = ...
    EX_SOFTWARE: Any = ...
    EX_OSERR: Any = ...
    EX_OSFILE: Any = ...
    EX_CANTCREAT: Any = ...
    EX_IOERR: Any = ...
    EX_TEMPFAIL: Any = ...
    EX_PROTOCOL: Any = ...
    EX_NOPERM: Any = ...
    EX_CONFIG: Any = ...

def exit(status: Union[int, ExitStatus], message: str=...) -> typing.NoReturn: ...
