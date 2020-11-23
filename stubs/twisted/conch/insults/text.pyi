from twisted.python import _textattributes
from typing import Any

flatten: Any

class _CharacterAttributes(_textattributes.CharacterAttributesMixin):
    fg: Any = ...
    bg: Any = ...
    attrs: Any = ...

attributes: Any
