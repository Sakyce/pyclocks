from .instance import Instance

from ..datatypes import Vector2, Color3

class Part(Instance):
    Position:Vector2
    Size:Vector2
    def __init__(self) -> None:
        super().__init__()
        self.Size = Vector2()
        self.Position = Vector2()
        self.Color = Color3.black()