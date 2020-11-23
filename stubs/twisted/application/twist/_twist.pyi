from ..runner._exit import ExitStatus as ExitStatus, exit as exit
from ..runner._runner import Runner as Runner
from ..service import Application as Application, IService as IService
from ._options import TwistOptions as TwistOptions
from twisted.python.usage import UsageError as UsageError
from typing import Any

class Twist:
    @staticmethod
    def options(argv: Any): ...
    @staticmethod
    def service(plugin: Any, options: Any): ...
    @staticmethod
    def startService(reactor: Any, service: Any) -> None: ...
    @staticmethod
    def run(twistOptions: Any) -> None: ...
    @classmethod
    def main(cls, argv: Any = ...) -> None: ...
