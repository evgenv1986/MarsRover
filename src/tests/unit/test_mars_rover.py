from src.marsRover.rover import \
    Cell, MoveCommand, Coordinate, Direction, Moveable, Plateau, Rover, Spatial




class TestMarsRover:
    def test_research_mars(self):
        pass
    def test_rover(self):
        rover = Rover(Direction.North)
        assert Direction.North.__eq__ (rover.Direction())


        moveableRover: Moveable = Rover(Direction.North)
        spatialPlateau: Spatial = Plateau(2, 2)
        spatialPlateau.Land(moveableRover)
        moveableRover.LandToPlateau(spatialPlateau)

        moveableRover.Move()
        
    def test_coordinate(self):
        assert Coordinate(0,1).__eq__(Coordinate(0,0))
        
    def test_command(self):
        command = MoveCommand.CreateByDirection(
                    Direction.North,
                    Coordinate(0,0))
        position: Coordinate = command.NextPosition()
        assert not Coordinate(0,0).__eq__(position)
        assert Coordinate(0,1).__eq__(position)
    
    def test_not_implemented_methods(self):
        rover = Rover(Direction.North)
        rover.Left()
        rover.Right()
        rover.Move()
        # rover.Execute(MoveCommand('L'))
        # rover.Execute(MoveCommand('R'))
        # rover.Execute(MoveCommand('M'))
        
        rover.LandToPlateau(Plateau(5,5))

        
    def test_plateau(self):
        plateau = Plateau(2, 2)
        rover = Rover(Direction.North)
        plateau.CheckPosition(rover.Coordinate())
        # plateau.AddRover(rover)
        
    # def test_cell_(self):
    #     Cell(Coordinate(1,1), Rover(Direction.North, Coordinate(0,0)))
        
        
    def test_can_move_from_left_bottom_on_north(self):
        rover = Rover(Direction.North)
        plateau = Plateau(2, 2)
        plateau.CheckPosition(rover.Coordinate())
        assert rover._plateau != None
        rover.Move()
        
        # plateau.RoverPosition() == ?
        # plateau.AddRover(rover)
    #     assert True == plateau.HasRover()
        # assert rover.Coordinate == 
        # rover.Left()
        # assert rover.Direction == Direction.West
        
    #     assert Coordinate(1, 2).__eq__(rover.Coordinate())
        
        # assert plateau.HasRover()
        # assert Coordinate(1, 1).__eq__ (plateau.Position())
        # assert Direction.North.__eq__ (plateau.RoverDirection())
        
   
    # def test_plate_add_rover(self):
    #     rover = Rover(Direction.North)
    #     plateau = Plateau(2, 2)
    #     plateau.AddRover(rover)
    #     assert True == plateau.HasRover()
        