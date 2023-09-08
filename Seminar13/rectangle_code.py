
class InvalidRectangleSide(Exception):
    def __init__(self, side):
        self.message = f"Invalid length of side: {side}. Side length should be positive."
        super().__init__(self.message)

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise InvalidRectangleSide(min(length, width))
        self.length = length
        self.width = width
        
class InvalidRectangleSide(Exception):
    def __init__(self, side):
        self.message = f"Invalid length of side: {side}. Side length should be positive."
        super().__init__(self.message)

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise InvalidRectangleSide(min(length, width))
        self.length = length
        self.width = width
