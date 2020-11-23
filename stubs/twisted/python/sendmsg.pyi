from collections import namedtuple
from socket import SCM_RIGHTS as SCM_RIGHTS
from typing import Any

RecievedMessage = namedtuple('RecievedMessage', ['data', 'ancillary', 'flags'])

def sendmsg(socket: Any, data: Any, ancillary: Any = ..., flags: int = ...): ...
def recvmsg(socket: Any, maxSize: int = ..., cmsgSize: int = ..., flags: int = ...): ...
def getSocketFamily(socket: Any): ...
