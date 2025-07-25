from marsRover.DirectionModule import Direction
from marsRover.Moveable import Moveable
from marsRover.Coordinate import Coordinate


from abc import ABC, abstractmethod


class Spatial(ABC):
    @abstractmethod
    def Land(cls, moveable: 'Moveable'):pass
    @abstractmethod
    def Move(cls,
            #  from_: Coordinate,
             direction: Direction,
             moveable):pass
    @abstractmethod
    def RoverPosition(self)-> Coordinate: pass