from ..runner._exit import ExitStatus as ExitStatus, exit as exit
from ..runner._runner import Runner as Runner
from ..service import Application as Application, IService as IService, IServiceMaker as IServiceMaker
from ._options import TwistOptions as TwistOptions
from twisted.internet.interfaces import IReactorCore as IReactorCore
from twisted.python.usage import Options as Options, UsageError as UsageError
from typing import Any, Sequence

class Twist:
    @staticmethod
    def options(argv: Sequence[str]) -> TwistOptions: ...
    @staticmethod
    def service(plugin: IServiceMaker, options: Options) -> IService: ...
    @staticmethod
    def startService(reactor: IReactorCore, service: IService) -> None: ...
    @staticmethod
    def run(twistOptions: TwistOptions) -> None: ...
    @classmethod
    def main(cls: Any, argv: Sequence[str]=...) -> None: ...
