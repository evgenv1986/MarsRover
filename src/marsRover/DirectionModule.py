
from abc import abstractmethod
from enum import Enum


class DirectionCommand(Enum):
    L = 1
    R = 2

class Direction():
    def CreateDirection(self, command: DirectionCommand):
        if command.name == 'R':
            return NorthDirection()
        raise ValueError("Invalid direction provided")
        
    @abstractmethod
    def change(sefl, command: DirectionCommand)-> 'Direction':
        pass
    
    @abstractmethod
    def name(self)->str:pass
    
    def __eq__(self, obj: object)-> bool:
        if isinstance(obj, Direction):
            other: Direction = obj
            return self.name() == other.name()
        return False

class SouthDirection(Direction):
    def change(self, command: DirectionCommand):
        if command == DirectionCommand.R:
            return WestDirection()
        if command == DirectionCommand.L:
            return EastDirection()
    def name(self)->str:
        return 'South'
    
class WestDirection(Direction):
    def change(self, command: DirectionCommand):
        if command == DirectionCommand.R:
            return NorthDirection()
        if command == DirectionCommand.L:
            return SouthDirection()
    def name(self)->str:
        return 'West'
    
class EastDirection(Direction):
    def change(self, command: DirectionCommand):
        if command == DirectionCommand.R:
            return SouthDirection()
        if command == DirectionCommand.L:
            return NorthDirection()
    def name(self)->str:
        return 'East'
    
class NorthDirection(Direction):
    def change(self, command: DirectionCommand):
        if command == DirectionCommand.R:
            return EastDirection()
        if command == DirectionCommand.L:
            return WestDirection()
    def name(self)->str:
        return 'North'
    
 