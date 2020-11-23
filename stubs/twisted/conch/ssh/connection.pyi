from twisted.conch import error as error
from twisted.conch.ssh import common as common, service as service
from twisted.internet import defer as defer
from twisted.python import log as log
from twisted.python.compat import long as long, nativeString as nativeString, networkString as networkString
from typing import Any

class SSHConnection(service.SSHService):
    name: bytes = ...
    localChannelID: int = ...
    localToRemoteChannel: Any = ...
    channels: Any = ...
    channelsToRemoteChannel: Any = ...
    deferreds: Any = ...
    transport: Any = ...
    def __init__(self) -> None: ...
    def serviceStarted(self) -> None: ...
    def serviceStopped(self) -> None: ...
    def ssh_GLOBAL_REQUEST(self, packet: Any) -> None: ...
    def ssh_REQUEST_SUCCESS(self, packet: Any) -> None: ...
    def ssh_REQUEST_FAILURE(self, packet: Any) -> None: ...
    def ssh_CHANNEL_OPEN(self, packet: Any) -> None: ...
    def ssh_CHANNEL_OPEN_CONFIRMATION(self, packet: Any) -> None: ...
    def ssh_CHANNEL_OPEN_FAILURE(self, packet: Any) -> None: ...
    def ssh_CHANNEL_WINDOW_ADJUST(self, packet: Any) -> None: ...
    def ssh_CHANNEL_DATA(self, packet: Any) -> None: ...
    def ssh_CHANNEL_EXTENDED_DATA(self, packet: Any) -> None: ...
    def ssh_CHANNEL_EOF(self, packet: Any) -> None: ...
    def ssh_CHANNEL_CLOSE(self, packet: Any) -> None: ...
    def ssh_CHANNEL_REQUEST(self, packet: Any): ...
    def ssh_CHANNEL_SUCCESS(self, packet: Any) -> None: ...
    def ssh_CHANNEL_FAILURE(self, packet: Any) -> None: ...
    def sendGlobalRequest(self, request: Any, data: Any, wantReply: int = ...): ...
    def openChannel(self, channel: Any, extra: bytes = ...) -> None: ...
    def sendRequest(self, channel: Any, requestType: Any, data: Any, wantReply: int = ...): ...
    def adjustWindow(self, channel: Any, bytesToAdd: Any) -> None: ...
    def sendData(self, channel: Any, data: Any) -> None: ...
    def sendExtendedData(self, channel: Any, dataType: Any, data: Any) -> None: ...
    def sendEOF(self, channel: Any) -> None: ...
    def sendClose(self, channel: Any) -> None: ...
    def getChannel(self, channelType: Any, windowSize: Any, maxPacket: Any, data: Any): ...
    def gotGlobalRequest(self, requestType: Any, data: Any): ...
    def channelClosed(self, channel: Any) -> None: ...

MSG_GLOBAL_REQUEST: int
MSG_REQUEST_SUCCESS: int
MSG_REQUEST_FAILURE: int
MSG_CHANNEL_OPEN: int
MSG_CHANNEL_OPEN_CONFIRMATION: int
MSG_CHANNEL_OPEN_FAILURE: int
MSG_CHANNEL_WINDOW_ADJUST: int
MSG_CHANNEL_DATA: int
MSG_CHANNEL_EXTENDED_DATA: int
MSG_CHANNEL_EOF: int
MSG_CHANNEL_CLOSE: int
MSG_CHANNEL_REQUEST: int
MSG_CHANNEL_SUCCESS: int
MSG_CHANNEL_FAILURE: int
OPEN_ADMINISTRATIVELY_PROHIBITED: int
OPEN_CONNECT_FAILED: int
OPEN_UNKNOWN_CHANNEL_TYPE: int
OPEN_RESOURCE_SHORTAGE: int
EXTENDED_DATA_STDERR: int
messages: Any
alphanums: Any
TRANSLATE_TABLE: Any
