from Point import Point

class Vector:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def XComp(self):
        return self.p2.x_coord - self.p1.x_coord

    def YComp(self):
        return self.p2.y_coord - self.p1.y_coord

    def crossProduct(self, vector):
        return self.XComp() * vector.YComp() - vector.XComp() * self.YComp()