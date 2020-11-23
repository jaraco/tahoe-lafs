from typing import Any, Optional
from zope.interface import Interface

class IAccount(Interface):
    client: Any = ...
    gatewayType: Any = ...
    def __init__(accountName: Any, autoLogin: Any, username: Any, password: Any, host: Any, port: Any) -> None: ...
    def isOnline() -> None: ...
    def logOn(chatui: Any) -> None: ...
    def logOff() -> None: ...
    def getGroup(groupName: Any) -> None: ...
    def getPerson(personName: Any) -> None: ...

class IClient(Interface):
    account: Any = ...
    def __init__(account: Any, chatui: Any, logonDeferred: Any) -> None: ...
    def joinGroup(groupName: Any) -> None: ...
    def leaveGroup(groupName: Any) -> None: ...
    def getGroupConversation(name: Any, hide: int = ...) -> None: ...
    def getPerson(name: Any) -> None: ...

class IPerson(Interface):
    def __init__(name: Any, account: Any) -> None: ...
    def isOnline() -> None: ...
    def getStatus() -> None: ...
    def getIdleTime() -> None: ...
    def sendMessage(text: Any, metadata: Optional[Any] = ...) -> None: ...

class IGroup(Interface):
    name: Any = ...
    account: Any = ...
    def __init__(name: Any, account: Any) -> None: ...
    def setTopic(text: Any) -> None: ...
    def sendGroupMessage(text: Any, metadata: Optional[Any] = ...) -> None: ...
    def join() -> None: ...
    def leave() -> None: ...

class IConversation(Interface):
    def __init__(person: Any, chatui: Any) -> None: ...
    def show() -> None: ...
    def hide() -> None: ...
    def sendText(text: Any, metadata: Any) -> None: ...
    def showMessage(text: Any, metadata: Any) -> None: ...
    def changedNick(person: Any, newnick: Any) -> None: ...

class IGroupConversation(Interface):
    def show() -> None: ...
    def hide() -> None: ...
    def sendText(text: Any, metadata: Any) -> None: ...
    def showGroupMessage(sender: Any, text: Any, metadata: Any) -> None: ...
    def setGroupMembers(members: Any) -> None: ...
    def setTopic(topic: Any, author: Any) -> None: ...
    def memberJoined(member: Any) -> None: ...
    def memberChangedNick(oldnick: Any, newnick: Any) -> None: ...
    def memberLeft(member: Any) -> None: ...

class IChatUI(Interface):
    def registerAccountClient(client: Any) -> None: ...
    def unregisterAccountClient(client: Any) -> None: ...
    def getContactsList() -> None: ...
    def getConversation(person: Any, Class: Any, stayHidden: int = ...) -> None: ...
    def getGroupConversation(group: Any, Class: Any, stayHidden: int = ...) -> None: ...
    def getPerson(name: Any, client: Any) -> None: ...
    def getGroup(name: Any, client: Any) -> None: ...
    def contactChangedNick(oldnick: Any, newnick: Any) -> None: ...
