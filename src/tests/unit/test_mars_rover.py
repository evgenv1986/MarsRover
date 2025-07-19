from src.marsRover.rover import Command, Coordinate, Direction, Rover




class TestMarsRover:
    def test_research_mars(self):
        rover = Rover(Direction.North)
        # assert Direction.North.__eq__ (rover.Direction())
        # rover.Left()
        # rover.Right()
        # rover.Move()
        # rover.Execute(Command('L'))
        # rover.Execute(Command('R'))
        # rover.Execute(Command('M'))
        
        # plateau = Plateau(2, 2)
        
        # plateau.AddRover(rover)
        # assert plateau.HasRover()
        # assert Coordinate(1, 1).__eq__ (plateau.Position())
        # assert Direction.North.__eq__ (plateau.RoverDirection())
        
   
    # def test_plate_add_rover(self):
    #     rover = Rover(Direction.North)
    #     plateau = Plateau(2, 2)
    #     plateau.AddRover(rover)
    #     assert True == plateau.HasRover()
        
    # def test_can_move_from_left_bottom_on_north(self):
    #     rover = Rover(Direction.North)
    #     plateau = Plateau(2, 2)
    #     plateau.AddRover(rover)
    #     assert True == plateau.HasRover()
    #     rover.Move()
    #     assert Coordinate(1, 2).__eq__(rover.Coordinate())
        
        