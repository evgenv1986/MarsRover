class Coordinate:
    _x: int
    _y: int
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    def __eq__(self, obj: object)-> bool:
        if isinstance(obj, Coordinate):
            other: Coordinate = obj
            return self._x == other._x and \
                   self._y == other._y
        return False