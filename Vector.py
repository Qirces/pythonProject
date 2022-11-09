class Vector():

    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x}, {self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)


v1 = Vector(1,1)
v2 = Vector(5,5)
v3 = Vector(10,10)

print(v3-v2)
print(v3 + v1)
print(v2*2)