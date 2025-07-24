from marsRover.DirectionModule import Direction, DirectionCommand, EastDirection, NorthDirection, SouthDirection, WestDirection

class TestRover:
    def test_direction(self):
        d: Direction = NorthDirection()
        d = d.change (DirectionCommand.R)
        assert EastDirection().name() == d.name()
        
        d = d.change(DirectionCommand.R)
        assert SouthDirection().name() == d.name()
        
        d = d.change(DirectionCommand.R)
        assert WestDirection().name() == d.name()
        
        d = d.change(DirectionCommand.R)
        assert NorthDirection().name() == d.name()
        
    def test_turn_left_and_right(self):
        d: Direction = SouthDirection()
        d = d.TurnRight()
        assert WestDirection().__eq__(d)
        
        
    def test_change_rover_direction(self):
        pass
        # rover: Moveable = Rover(Direction.North)
        # rover.changeDirection ('R') 
        # assert Direction.East.__eq__(rover.Direction())
    
    