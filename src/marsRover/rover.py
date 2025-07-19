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
    @abstractmethod
    def NextPosition(self): pass
  
class MoveIncYCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self): pass
class MoveIncXCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self): pass
class MoveDecXCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self): pass
class MoveDecYCommand(MoveCommand):
    def __init__(self, coordinate: 'Coordinate'):pass
    def NextPosition(self): pass
   
class Coordinate:
    def __init__(self, x: int, y: int):pass
    def __eq__(self, obj: object)-> bool:
        other = obj
        return True
        
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
    
    def Move(self, 
            #  from_: Coordinate,
             direction: Direction,
             moveable):
        # pass
        command = MoveCommand.CreateByDirection(
                    direction,
                    self._checked_position)
        next_ = command.NextPosition()
        # 1,0   1,1
        # 0,0   1,0
        # moveIncYCommand = Move (Direction.North) -> from_.IncY()
        # moveIncXCommand = Move (Direction.East) -> from_.IncX()
        # moveDecXCommand = Move (Direction.West) -> from_.DecX()
        # moveDecYCommand = Move (Direction.South) -> from_.DecY()
        # command.execute()
        # nextCoordinate = Coordinate(1,0)
        # moveable.ChangePosition(newCoordinate())


class Moveable(ABC):
    @abstractmethod
    def Move(cls):pass
    @abstractmethod
    def LandToPlateau(clas, spatial: 'Spatial'):pass

class Rover (Moveable):
    _direction: Direction
    _plateau: Spatial
    _coordinate: Coordinate
    def __init__ (self, direction: Direction):
        self._direction = direction
        # self._coordinate = coordinate
        
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
        # self._plateau.AddRover(self)

    
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

        