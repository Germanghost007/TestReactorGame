from math import sqrt, pow

class Position:

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z:float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, pos: 'Position') -> float:
        return sqrt(pow(self.x - pos.x, 2) + pow(self.y - pos.y, 2) + pow(self.z - pos.z, 2))
    