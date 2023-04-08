from .vector2 import Vector2

class UDim2:
    Scale:Vector2
    Offset:Vector2

    def __init__(self, XScale, YScale, XOffset, YOffset) -> None:
        self.Scale = Vector2(XScale, YScale)
        self.Offset = Vector2(XOffset, YOffset)

    @staticmethod
    def fromScale(X:float, Y:float):
        return UDim2(X,Y,0,0)

    @staticmethod
    def fromOffset(X:float, Y:float):
        return UDim2(0,0,X,Y)
    
    @staticmethod
    def zero():
        return UDim2(0,0,0,0)
    
    def __repr__(self) -> str:
        return f"UDim2(Scale: {self.Scale.X}x{self.Scale.Y} Offset: {self.Offset.X}x{self.Offset.Y})"