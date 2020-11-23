from twisted.application.app import ReactorSelectionMixin as ReactorSelectionMixin
from twisted.python.filepath import FilePath as FilePath
from twisted.python.usage import Options as Options
from twisted.scripts.trial import _BasicOptions

class WorkerOptions(_BasicOptions, Options, ReactorSelectionMixin):
    def coverdir(self): ...
