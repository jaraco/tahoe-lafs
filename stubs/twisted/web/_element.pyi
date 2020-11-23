from twisted.web.error import MissingRenderMethod as MissingRenderMethod, MissingTemplateLoader as MissingTemplateLoader, UnexposedMethodError as UnexposedMethodError
from twisted.web.iweb import IRenderable as IRenderable, ITemplateLoader as ITemplateLoader
from typing import Any, Optional

class Expose:
    doc: Any = ...
    def __init__(self, doc: Optional[Any] = ...) -> None: ...
    def __call__(self, *funcObjs: Any): ...
    def get(self, instance: Any, methodName: Any, default: Any = ...): ...

exposer: Any

def renderer() -> None: ...

class Element:
    loader: Optional[ITemplateLoader] = ...
    def __init__(self, loader: Optional[Any] = ...) -> None: ...
    def lookupRenderMethod(self, name: Any): ...
    def render(self, request: Any): ...
