from typing import Any

class SecureRandomNotAvailable(RuntimeError): ...
class SourceNotAvailable(RuntimeError): ...

class RandomFactory:
    randomSources: Any = ...
    getrandbits: Any = ...
    def secureRandom(self, nbytes: Any, fallback: bool = ...): ...
    def insecureRandom(self, nbytes: Any): ...

secureRandom: Any
insecureRandom: Any
