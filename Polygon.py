from Point import Point
from Vector import Vector

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def move(self, vector):
        for vertex in self.vertices:
            vertex.x_coord += vector.XComp()
            vertex.y_coord += vector.YComp()

    def centroid(self):
        n = len(self.vertices)
        
        a = 0
        for i in range(n):
            a += self.vertices[i].x_coord*self.vertices[(i+1)%n].y_coord-self.vertices[(i+1)%n].x_coord*self.vertices[i].y_coord
        a /= 2

        x = 0
        for i in range(n):
            x += (self.vertices[(i+1)%n].x_coord+self.vertices[i].x_coord)*(self.vertices[i].x_coord*self.vertices[(i+1)%n].y_coord-self.vertices[(i+1)%n].x_coord*self.vertices[i].y_coord)
        x /= 6*a

        y = 0
        for i in range(n):
            y += (self.vertices[(i+1)%n].y_coord+self.vertices[i].y_coord)*(self.vertices[i].x_coord*self.vertices[(i+1)%n].y_coord-self.vertices[(i+1)%n].x_coord*self.vertices[i].y_coord)
        y /= 6*a
      
        return Point(x, y)