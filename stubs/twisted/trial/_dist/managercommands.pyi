from twisted.protocols.amp import Boolean as Boolean, Command as Command, ListOf as ListOf, Unicode as Unicode
from typing import Any

NativeString = Unicode

class AddSuccess(Command):
    arguments: Any = ...
    response: Any = ...

class AddError(Command):
    arguments: Any = ...
    response: Any = ...

class AddFailure(Command):
    arguments: Any = ...
    response: Any = ...

class AddSkip(Command):
    arguments: Any = ...
    response: Any = ...

class AddExpectedFailure(Command):
    arguments: Any = ...
    response: Any = ...

class AddUnexpectedSuccess(Command):
    arguments: Any = ...
    response: Any = ...

class TestWrite(Command):
    arguments: Any = ...
    response: Any = ...
