from abc import ABC, abstractmethod
from enum import Enum

from git import Object

from marsRover.Coordinate import Coordinate
from marsRover.DirectionModule import Direction, EastDirection, NorthDirection, SouthDirection, WestDirection

class MoveCommand(ABC):
    def __init__(self, direction: Direction, coordinate: 'Coordinate'):pass
    @classmethod
    def CreateByDirection(cls, direction: Direction, coordinate: 'Coordinate'):
        if NorthDirection().name() == direction.name():
            return MoveIncYCommand(coordinate)
        if EastDirection().name() == direction.name():
            return MoveIncXCommand(coordinate)
        if WestDirection().name() == direction.name():
            return MoveDecXCommand(coordinate)
        if SouthDirection().name() == direction.name():
            return MoveDecYCommand(coordinate)
        raise ValueError("Invalid direction provided")
    @abstractmethod
    def NextPosition(self)->Coordinate: pass
  
class MoveIncYCommand(MoveCommand):
    _coordinate: Coordinate
    def __init__(self, coordinate: 'Coordinate'):
        self._coordinate = coordinate
    def NextPosition(self): 
        return Coordinate(
            self._coordinate._x,
            self._coordinate._y + 1)
class MoveIncXCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self):  return Coordinate(0,0)
class MoveDecXCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self):  return Coordinate(0,0)
class MoveDecYCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self):  return Coordinate(0,0)
   

    
        

        
    