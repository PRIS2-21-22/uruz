from Point import Point
from Vector import Vector

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def move(self, vector):
        for vertex in self.vertices:
            vertex.x += vector.X()
            vertex.y += vector.Y()

class main():
    vertices = [Point(1,1), Point(0,0), Point(0,1)]
    polygon = Polygon(vertices)
    polygon.move(Vector(Point(0,0),Point(1,1)))
    for vertex in polygon.vertices:
        print(vertex.x)
        print(vertex.y)