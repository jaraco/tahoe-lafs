from twisted.web import static as static

class Test(static.Data):
    isLeaf: bool = ...
    def __init__(self) -> None: ...
