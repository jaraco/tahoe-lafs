from twisted import copyright as copyright
from twisted.python import htmlizer as htmlizer, usage as usage
from typing import Any

header: str
footer: str
styleLink: str
alternateLink: str

class Options(usage.Options):
    synopsis: Any = ...
    optParameters: Any = ...
    compData: Any = ...
    def parseArgs(self, filename: Any) -> None: ...

def run() -> None: ...
