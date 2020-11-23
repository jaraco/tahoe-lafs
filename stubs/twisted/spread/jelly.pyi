from twisted.persisted.crefutil import NotKnown as NotKnown
from twisted.python.compat import nativeString as nativeString
from twisted.python.deprecate import deprecatedModuleAttribute as deprecatedModuleAttribute
from twisted.python.reflect import namedAny as namedAny, namedObject as namedObject, qual as qual
from twisted.spread.interfaces import IJellyable as IJellyable, IUnjellyable as IUnjellyable
from typing import Any, Optional

DictTypes: Any
None_atom: bytes
class_atom: bytes
module_atom: bytes
function_atom: bytes
dereference_atom: bytes
persistent_atom: bytes
reference_atom: bytes
dictionary_atom: bytes
list_atom: bytes
set_atom: bytes
tuple_atom: bytes
instance_atom: bytes
frozenset_atom: bytes
unpersistable_atom: bytes
unjellyableRegistry: Any
unjellyableFactoryRegistry: Any

def setUnjellyableForClass(classname: Any, unjellyable: Any) -> None: ...
def setUnjellyableFactoryForClass(classname: Any, copyFactory: Any) -> None: ...
def setUnjellyableForClassTree(module: Any, baseClass: Any, prefix: Optional[Any] = ...) -> None: ...
def getInstanceState(inst: Any, jellier: Any): ...
def setInstanceState(inst: Any, unjellier: Any, jellyList: Any): ...

class Unpersistable:
    reason: Any = ...
    def __init__(self, reason: Any) -> None: ...

class Jellyable:
    def getStateFor(self, jellier: Any): ...
    def jellyFor(self, jellier: Any): ...

class Unjellyable:
    __dict__: Any = ...
    def setStateFor(self, unjellier: Any, state: Any) -> None: ...
    def unjellyFor(self, unjellier: Any, jellyList: Any): ...

class _Jellier:
    taster: Any = ...
    preserved: Any = ...
    cooked: Any = ...
    cooker: Any = ...
    persistentStore: Any = ...
    invoker: Any = ...
    def __init__(self, taster: Any, persistentStore: Any, invoker: Any) -> None: ...
    def prepare(self, object: Any): ...
    def preserve(self, object: Any, sexp: Any): ...
    def jelly(self, obj: Any): ...
    def jelly_decimal(self, d: Any): ...
    def unpersistable(self, reason: Any, sxp: Optional[Any] = ...): ...

class _Unjellier:
    taster: Any = ...
    persistentLoad: Any = ...
    references: Any = ...
    postCallbacks: Any = ...
    invoker: Any = ...
    def __init__(self, taster: Any, persistentLoad: Any, invoker: Any) -> None: ...
    def unjellyFull(self, obj: Any): ...
    def unjelly(self, obj: Any): ...
    def unjellyInto(self, obj: Any, loc: Any, jel: Any): ...

class InsecureJelly(Exception): ...

class DummySecurityOptions:
    def isModuleAllowed(self, moduleName: Any): ...
    def isClassAllowed(self, klass: Any): ...
    def isTypeAllowed(self, typeName: Any): ...

class SecurityOptions:
    basicTypes: Any = ...
    allowedTypes: Any = ...
    allowedModules: Any = ...
    allowedClasses: Any = ...
    def __init__(self) -> None: ...
    def allowBasicTypes(self) -> None: ...
    def allowTypes(self, *types: Any) -> None: ...
    def allowInstancesOf(self, *classes: Any) -> None: ...
    def allowModules(self, *modules: Any) -> None: ...
    def isModuleAllowed(self, moduleName: Any): ...
    def isClassAllowed(self, klass: Any): ...
    def isTypeAllowed(self, typeName: Any): ...

globalSecurity: Any

def jelly(object: Any, taster: Any = ..., persistentStore: Optional[Any] = ..., invoker: Optional[Any] = ...): ...
def unjelly(sexp: Any, taster: Any = ..., persistentLoad: Optional[Any] = ..., invoker: Optional[Any] = ...): ...
