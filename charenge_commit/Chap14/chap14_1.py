class Square:
    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.square_list.append((self.width, self.length))

square1 = Square(10, 10)
square2 = Square(30, 30)
square3 = Square(60, 60)

print(Square.square_list)