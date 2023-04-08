from .instance import Instance
from ..datatypes import Color3, UDim2, Vector2
from ..settings import Settings

class Object2D(Instance):
    _pos:UDim2
    _size:UDim2

    def __init__(self) -> None:
        super().__init__()
        self.Size = UDim2.zero()
        self.Position = UDim2.zero()
        self.AbsolutePosition = Vector2()
        self.AbsoluteSize = Vector2()

    @property
    def Position(self): return self._pos
    @Position.setter
    def Position(self, v:UDim2):
        self._pos = v

        parent_size = getattr(Frame.Parent, '_AbsoluteSize', Settings.WindowSize)

        self.AbsolutePosition = Vector2(
            self._pos.Scale.X * parent_size.X + self._pos.Offset.X,
            self._pos.Scale.Y * parent_size.Y + self._pos.Offset.Y
        )

    @property
    def Size(self): return self._size
    @Size.setter
    def Size(self, v:UDim2):
        self._size = v

        parent_size = getattr(Frame.Parent, '_AbsoluteSize', Settings.WindowSize)

        self.AbsoluteSize = Vector2(
            self._size.Scale.X * parent_size.X + self._size.Offset.X,
            self._size.Scale.Y * parent_size.Y + self._size.Offset.Y
        )

class Frame(Object2D):
    def __init__(self) -> None:
        super().__init__()
        self.Color = Color3.black()