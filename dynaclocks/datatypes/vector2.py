import math
from random import randint

from ..exceptions.readonly import readonly

class Vector2:
    X:float
    Y:float

    def __init__(self,x:float=0,y:float=0) -> None:
        self.X = x
        self.Y = y
    
    @readonly
    def Magnitude(self):
        return math.sqrt(self.X**2 + self.Y**2)
    
    @staticmethod
    def RandomBetween(x:float, y:float, x2:float, y2:float):
        x, x2 = int(x), int(x2)
        y, y2 = int(y), int(y2)
        
        return Vector2(randint(x, x2), randint(y, y2))
    
    @staticmethod
    def zero():
        return Vector2()

    def __iter__(self):
        return iter([self.X, self.Y])
    
    def __repr__(self) -> str:
        return f"Vector2({self.X},{self.Y})"