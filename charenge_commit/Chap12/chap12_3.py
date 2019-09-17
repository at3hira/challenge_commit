"""
・Create triangle object and Define a class
・find the triangle area output result

"""

class Triangle:
    def __init__(self, base, height):
        """
        Parameters
        --------------
            base : int
            triangle base

            height : int
            triangle height
        """
        self.base = base
        self.height = height
    

    def area(self):
        """
        return
        --------------
            return : float
            triangle area
        """
        return self.base * self.height / 2

triangle = Triangle(20, 10)
triangle_area = triangle.area()
print(triangle_area)