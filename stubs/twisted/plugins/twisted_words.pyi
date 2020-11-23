from twisted.application.service import ServiceMaker as ServiceMaker
from twisted.plugin import IPlugin as IPlugin
from twisted.words import iwords as iwords
from typing import Any

NewTwistedWords: Any
TwistedXMPPRouter: Any

class RelayChatInterface:
    name: str = ...
    @classmethod
    def getFactory(cls, realm: Any, portal: Any): ...

class PBChatInterface:
    name: str = ...
    @classmethod
    def getFactory(cls, realm: Any, portal: Any): ...
