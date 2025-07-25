from marsRover.Coordinate import Coordinate
from marsRover.DirectionModule import Direction
from marsRover.Moveable import Moveable
from marsRover.Spatial import Spatial
from marsRover.rover import MoveCommand


class Rover (Moveable):
    _direction: Direction
    _plateau: Spatial
    _coordinate: Coordinate
    def __init__ (self, direction: Direction):
        self._direction = direction
    def Move(self):
        self._plateau.Move(
            self._direction,
            self)
    def Direction(self)-> Direction:
        return self._direction
    def Coordinate(self):
        return self._plateau.RoverPosition()
    def Execute(self, command: MoveCommand):pass
    def LandToPlateau(self, spatial: Spatial):
        self._plateau = spatial

    def changeDirection(self, title: str):
        pass

    def Left(self):
        raise NotImplementedError

    def Right(self):
        raise NotImplementedError