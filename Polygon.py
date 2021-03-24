from Point import Point
from Vector import Vector

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def move(self, vector):
        for vertex in self.vertices:
            vertex.x += vector.X()
            vertex.y += vector.Y()

    def centroid(self):
        n = len(self.vertices)
        
        a = 0
        for i in range(n):
            a += self.vertices[i].x*self.vertices[(i+1)%n].y-self.vertices[(i+1)%n].x*self.vertices[i].y
        a /= 2

        x = 0
        for i in range(n):
            x += (self.vertices[(i+1)%n].x+self.vertices[i].x)*(self.vertices[i].x*self.vertices[(i+1)%n].y-self.vertices[(i+1)%n].x*self.vertices[i].y)
        x /= 6*a

        y = 0
        for i in range(n):
            y += (self.vertices[(i+1)%n].y+self.vertices[i].y)*(self.vertices[i].x*self.vertices[(i+1)%n].y-self.vertices[(i+1)%n].x*self.vertices[i].y)
        y /= 6*a
      
        return Point(x, y)

class main:
    vertices = [Point(1,1), Point(0,0), Point(0,1)]
    polygon = Polygon(vertices)
    polygon.move(Vector(Point(0,0),Point(1,1)))
    for vertex in polygon.vertices:
        print(vertex.x)
        print(vertex.y)
    print(polygon.centroid().x)
    print(polygon.centroid().y)