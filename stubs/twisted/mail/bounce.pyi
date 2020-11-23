from twisted.mail import smtp as smtp
from typing import Any

BOUNCE_FORMAT: str

def generateBounce(message: Any, failedFrom: Any, failedTo: Any, transcript: str = ..., encoding: str = ...): ...
