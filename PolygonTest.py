from Point import Point
from Vector import Vector
from Polygon import Polygon

class main:
    vertices = [Point(1,1), Point(0,0), Point(0,1)]
    polygon = Polygon(vertices)
    polygon.move(Vector(Point(0,0), Point(1,1)))
    
    print(polygon.centroid().x_coord)
    print(polygon.centroid().y_coord)