from src.marsRover.rover import \
    Cell, DirectionCommand, MoveCommand, Coordinate, Direction, Moveable, Plateau, Rover, Spatial




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

        # move on north and check position
        moveableRover.Move()
        assert moveableRover.Coordinate().__eq__(Coordinate(0, 1))
        
        assert Direction.North.__eq__ (moveableRover.Direction())
        
        
    def test_coordinate(self):
        assert Coordinate(0,0).__eq__(Coordinate(0,0))
        assert not Coordinate(0,1).__eq__(Coordinate(0,0))
        
    def test_command(self):
        command = MoveCommand.CreateByDirection(
                    Direction.North,
                    Coordinate(0,0))
        position: Coordinate = command.NextPosition()
        assert not Coordinate(0,0).__eq__(position)
        assert Coordinate(0,1).__eq__(position)
    
    