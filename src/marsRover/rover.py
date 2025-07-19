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
    
class Command:
    def __init__(self, name: str):pass    
   
class Rover:
    _direction: Direction
    _plateau: 'Plateau'
    def __init__ (self, direction: Direction):
        self._direction = direction
    def Left(self):pass
    def Right(self):pass
    def Move(self):
        pass # self._plateau.Move(self, self._direction)
        
    def Direction(self)-> Direction: 
        return self._direction
    def Coordinate(self): 
        pass #return self._plateau.Position()
    def Execute(self, command: Command):pass
    
class Coordinate:
    def __init__(self, x: int, y: int):pass
    def __eq__(self, obj: object)-> bool:
        other = obj
        return True
        
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

        
class Plateau:
    _cell: Cell
    def __init__(self, width: int, height: int):pass
    def AddRover(self, rover: Rover):
        self._cell = Cell(
            self._cell.Position(), 
            rover)
    def HasRover(self): 
        return self._cell.HasRover()
    def Position(self): 
        pass
    def RoverDirection(self): pass
    
    # def Move(self, 
    #          placeable: Placeable, 
    #          direction: Direction):pass
    
    
    
    # class Volumeable:
    # def Move(self, 
    #          placeable: Placeable, 
    #          direction: Direction):pass
    # def Position(self):
    #     return
    # def HasRover(self):
    #     return True
    
    
     
# class Placeable:
#     _rover: 'Rover'
#     _coordinate: 'Coordinate'
#     def Position(self)-> 'Coordinate':pass    
