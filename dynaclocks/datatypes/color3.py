class Color3:
    def __init__(self, r:float,g:float,b:float) -> None:
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    @staticmethod
    def black():
        return Color3(0,0,0)
    
    def __iter__(self):
        return iter([self.r, self.g, self.b])
    
    def __mul__(self, v:float):
        r = self.r * v
        g = self.g * v
        b = self.b * v
        return Color3(r,g,b)
    
    def __repr__(self) -> str:
        return f"Color3({self.r*255},{self.g*255},{self.b*255})"