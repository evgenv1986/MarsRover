from marsRover.Coordinate import Coordinate
from marsRover.DirectionModule import Direction
from marsRover.Moveable import Moveable
from marsRover.Spatial import Spatial
from marsRover.rover import MoveCommand


class Plateau(Spatial):
    _moveable: 'Moveable'
    _moveableCoordinate: Coordinate
    _commands: list
    _width: int
    _height: int
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    def Land(self, moveable: 'Moveable'):
        self._moveable = moveable
        self._moveableCoordinate = Coordinate(0,0)
    def Move(self,
             direction: Direction,
             moveable: 'Moveable'):
        command = MoveCommand.CreateByDirection(
                    direction,
                    self._moveableCoordinate)
        self._moveableCoordinate = command.NextPosition()
    def RoverPosition(self):
        return self._moveableCoordinate
    def HasRover(self): pass
    def Position(self): pass
    def RoverDirection(self): pass