from Point import Point

class Vector:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def x_comp(self):
        return self.p2.x_coord - self.p1.x_coord

    def y_comp(self):
        return self.p2.y_coord - self.p1.y_coord

    def cross_product(self, vector):
        return self.x_comp() * vector.YComp() - vector.XComp() * self.y_comp()