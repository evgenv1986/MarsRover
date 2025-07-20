from abc import ABC, abstractmethod
from enum import Enum

from git import Object

class Direction(Enum):
    North = 1
    East = 2
    West = 3
    South = 4
    def __eq__(self, obj: object)-> bool:
        other: Direction = Direction (obj)
        return True
    

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
    
    
class MoveCommand(ABC):
    def __init__(self, direction: Direction, coordinate: 'Coordinate'):pass
    @classmethod
    def CreateByDirection(cls, direction: Direction, coordinate: 'Coordinate'):
        if direction.North:
            return MoveIncYCommand(coordinate)
        if direction.East:
            return MoveIncXCommand(coordinate)
        if direction.West:
            return MoveDecXCommand(coordinate)
        if direction.South:
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
   
        
class Spatial(ABC):
    @abstractmethod
    def Land(cls, moveable: 'Moveable'):pass
    @abstractmethod
    def Move(cls,
            #  from_: Coordinate,
             direction: Direction,
             moveable):pass
      
class Plateau(Spatial):
    # _cell: Cell
    _checked_position: Coordinate
    _moveable: 'Moveable'
    _moveableCoordinate: Coordinate
    def __init__(self, width: int, height: int):pass
    def Land(self, moveable: 'Moveable'):
        self._moveable = moveable
        self._moveableCoordinate = Coordinate(0,0)
    def Move(self, 
            #  from_: Coordinate,
             direction: Direction,
             moveable):
        command = MoveCommand.CreateByDirection(
                    direction,
                    self._checked_position)
        # command.NextPosition()
        # _moveableCoordinate = command.NextPosition()
        # 1,0   1,1
        # 0,0   1,0
        # moveIncYCommand = Move (Direction.North) -> from_.IncY()
        # moveIncXCommand = Move (Direction.East) -> from_.IncX()
        # moveDecXCommand = Move (Direction.West) -> from_.DecX()
        # moveDecYCommand = Move (Direction.South) -> from_.DecY()
        # command.execute()
        # nextCoordinate = Coordinate(1,0)
        # moveable.ChangePosition(newCoordinate())
        
    def AddRover(self, rover: 'Rover'):
        self._cell = Cell(
            Coordinate(0, 0), 
            rover)
    def CheckPosition(self, checking: Coordinate):
        self._checked_position = checking   
    def HasRover(self): 
        return self._cell.HasRover()
    def Position(self): 
        pass
    def RoverDirection(self): pass
    
    


class Moveable(ABC):
    @abstractmethod
    def Move(cls):pass
    @abstractmethod
    def Left(cls):pass
    @abstractmethod
    def Right(cls):pass
    @abstractmethod
    def LandToPlateau(clas, spatial: 'Spatial'):pass

class Rover (Moveable):
    _direction: Direction
    _plateau: Spatial
    _coordinate: Coordinate
    def __init__ (self, direction: Direction):
        self._direction = direction
    def Left(self):pass
    def Right(self):pass
    def Move(self):
        self._plateau.Move(
            self._direction, 
            self)
        
    def Direction(self)-> Direction: 
        return self._direction
    def Coordinate(self): 
        return self._coordinate
    def Execute(self, command: MoveCommand):pass
    def LandToPlateau(self, spatial: Spatial):
        self._plateau = spatial

    
class EmptyCell:
    _coordinate: Coordinate
    _rover: Rover
    def __init__(self, c: Coordinate):pass
    def Position(self): pass 
    def Land(self, rover: Rover):pass
    def Remove(self):pass
    def HasRover(self):
        return True
    
class Cell:
    _coordinate: Coordinate
    _rover: Rover
    def __init__(self, c: Coordinate, rover: Rover):pass
    def Position(self): 
        return self._coordinate
    def Land(self, rover: Rover):pass
    def Remove(self):pass
    def HasRover(self):
        return True    

        