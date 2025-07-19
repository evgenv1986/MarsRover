def test_sample_unit():
    assert 1 + 1 == 2

class TestStringOperations:
    def test_reverse(self):
        assert "hello"[::-1] == "olleh"
    
    def test_upper(self):
        assert "foo".upper() == "FOO"