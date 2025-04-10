#Crucial remember:
from __future__ import annotations

# x y coordinate points
class Point:
    # def __init__(self):
    #     '''
    #     Create a two dimensional point at coordinates (0, 0)
    #     '''
    #     self.x = 0
    #     self.y = 0

    def __init__(self, x: int, y: int):
        '''
        Create 2d point at (x,y)
        '''
        self.x = x
        self.y = y

    def translate(self, dx: int, dy: int):
        '''
        Move point horizontally and vertically according to dx and dy
        '''
        self.x += dx
        self.y += dy

    def distance(self, other_point: Point)-> float:
        x_d = self.x - other_point.x
        y_d = self.y - other_point.y
        return (x_d**2 + y_d**2)**0.5 #Pythoagore
    
    def __repr__(self)-> str:
        #This specific section is related to how print() will print this object
        return f"({self.x}, {self.y})"
    
    def __lt__(self, other_point: Point)-> bool:
        '''
        true of self point x and y coordinates are less
        than other point x and y (x1 < x2 and y1 < y2)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
        <, __lt__
        ==, __eq__
        ...
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        return isinstance(other_point, Point) and self.x < other_point.x and self.y < other_point.y
    
    def __eq__(self, other_point: Point)-> bool:
        '''
        comparing two points (==)
        '''
        return isinstance(other_point, Point) and self.x == other_point.x and self.y == other_point.y

class Segment:
    #if Point was in another file, you can wirte "from {file_name_with_point} import Point". {file_name_with_point} is the filename without the .py
    '''
    Will be used to represent a line segment between two points
    Will utilize previously defined point object
    '''

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def translate(self, dx: int, dy: int):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
        #Example of a "has-a" relationship between points

    def length(self)-> float:
        return(self.p1, self.p2)

#~~~~~~~~~~~~~~~~~~~~~
#Main program:

p1 = Point(1,1)
# p1.translate(1,0)
# print(f"(x,y) coordinates of p1 are ({p1.x}, {p1.y})")

p2 = Point(2,1)
# print(p1.distance(p2))

# print(p1)

# print(p1 < p2)
