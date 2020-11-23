from twisted.internet.defer import Deferred as Deferred
from twisted.internet.interfaces import IAddress as IAddress, ITransport as ITransport
from twisted.internet.protocol import ProcessProtocol as ProcessProtocol
from twisted.protocols.amp import AMP as AMP
from twisted.python.failure import Failure as Failure
from twisted.python.reflect import namedObject as namedObject
from twisted.trial._dist import managercommands as managercommands, workercommands as workercommands
from twisted.trial._dist.workerreporter import WorkerReporter as WorkerReporter
from twisted.trial.runner import TestLoader as TestLoader, TrialSuite as TrialSuite
from twisted.trial.unittest import Todo as Todo
from typing import Any

class WorkerProtocol(AMP):
    def __init__(self, forceGarbageCollection: bool = ...) -> None: ...
    def run(self, testCase: Any): ...
    def start(self, directory: Any): ...

class LocalWorkerAMP(AMP):
    def addSuccess(self, testName: Any): ...
    def addError(self, testName: Any, error: Any, errorClass: Any, frames: Any): ...
    def addFailure(self, testName: Any, fail: Any, failClass: Any, frames: Any): ...
    def addSkip(self, testName: Any, reason: Any): ...
    def addExpectedFailure(self, testName: Any, error: Any, todo: Any): ...
    def addUnexpectedSuccess(self, testName: Any, todo: Any): ...
    def testWrite(self, out: Any): ...
    def run(self, testCase: Any, result: Any): ...
    def setTestStream(self, stream: Any) -> None: ...

class LocalWorkerAddress: ...

class LocalWorkerTransport:
    def __init__(self, transport: Any) -> None: ...
    def write(self, data: Any) -> None: ...
    def writeSequence(self, sequence: Any) -> None: ...
    def loseConnection(self) -> None: ...
    def getHost(self): ...
    def getPeer(self): ...

class LocalWorker(ProcessProtocol):
    endDeferred: Any = ...
    def __init__(self, ampProtocol: Any, logDirectory: Any, logFile: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def connectionLost(self, reason: Any) -> None: ...
    def processEnded(self, reason: Any) -> None: ...
    def outReceived(self, data: Any) -> None: ...
    def errReceived(self, data: Any) -> None: ...
    def childDataReceived(self, childFD: Any, data: Any) -> None: ...
