
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape): # Inherit Shape class
    pass
class Square(Shape): # Inherit Shape class
    pass

rectangle = Rectangle()
rectangle.what_am_i() # call the Shape class method

square = Square()
square.what_am_i() # call the Shape class method
