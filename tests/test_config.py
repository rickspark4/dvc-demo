
#it is important to write "test" in def function

import pytest

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 2
    b = 2
    assert a == b
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange