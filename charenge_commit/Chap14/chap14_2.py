class Square:

    def __init__(self, one_side):
        self.one_side = one_side

    def __repr__(self):
        return "{} by {} by {} by {}" .format(self.one_side, self.one_side, self.one_side, self.one_side)

square = Square(20)
print(square)
