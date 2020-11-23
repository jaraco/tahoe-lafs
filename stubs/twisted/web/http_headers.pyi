from typing import Any, AnyStr, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

class Headers:
    def __init__(self, rawHeaders: Optional[Mapping[AnyStr, Sequence[AnyStr]]]=...) -> None: ...
    def __cmp__(self, other: Any): ...
    def copy(self): ...
    def hasHeader(self, name: AnyStr) -> bool: ...
    def removeHeader(self, name: AnyStr) -> None: ...
    def setRawHeaders(self, name: AnyStr, values: Sequence[AnyStr]) -> None: ...
    def addRawHeader(self, name: AnyStr, value: AnyStr) -> None: ...
    def getRawHeaders(self, name: AnyStr, default: Optional[_T]=...) -> Union[List[AnyStr], Optional[_T]]: ...
    def getAllRawHeaders(self) -> Iterator[Tuple[bytes, List[bytes]]]: ...
