from Point import Point

class Vector:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def X(self):
        return self.p2.x - self.p1.x

    def Y(self):
        return self.p2.y - self.p1.y

    def crossProduct(self, vector):
        return self.X() * vector.Y() - vector.X() * self.Y()