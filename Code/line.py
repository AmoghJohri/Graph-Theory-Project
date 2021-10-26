from point import Point

class Line:
    def __init__(self, p1, p2, offset=0.00001):
        self.p1 = p1
        self.p2 = p2 
        if self.p1.x == self.p2.x:
            self.p1.x += offset
        self.bottom = min(self.p1.y, self.p2.y)
        self.top = max(self.p1.y, self.p2.y)
        self.left = min(self.p1.x, self.p2.x)
        self.right = max(self.p1.x, self.p2.x)
        self.m = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
        self.c = self.p1.y - self.m*self.p1.x

    @staticmethod
    def isIntersecting(l1, l2, offset=0.00001):
        if not (l1.bottom > l2.top or l2.bottom > l1.top or l1.left > l2.right or l2.left > l1.right):
            if l1.m == l2.m:
                x1 = (l2.c - l1.c)/((l1.m - l2.m) - 2*offset)
                x2 = (l2.c - l1.c)/((l1.m - l2.m) + 2*offset)
                if (x1 <= min(l1.right, l2.right) and x1 >= max(l1.left, l2.left)):
                    return True 
                elif (x2 <= min(l1.right, l2.right) and x2 >= max(l1.left, l2.left)):
                    return True
            else:
                x = (l2.c - l1.c)/(l1.m - l2.m)
                if (x <= min(l1.right, l2.right) and x >= max(l1.left, l2.left)):
                    return True 
        return False

if __name__ == "__main__":
    line1 = Line(Point(0, 0), Point(4, 1))
    line2 = Line(Point(5, 0), Point(3, 1))
    print(Line.isIntersecting(line1, line2))