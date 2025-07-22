class TestRover:
    def test_change_rover_direction(self):
        rover: Moveable = Rover(Direction.North)
        rover.changeDirection ('R') 
        assert Direction.East.__eq__(rover.Direction())
    
    