from ._team import Team as Team
from ._threadworker import LockWorker as LockWorker, ThreadWorker as ThreadWorker
from twisted.python.log import err as err
from typing import Any

def pool(currentLimit: Any, threadFactory: Any = ...): ...
