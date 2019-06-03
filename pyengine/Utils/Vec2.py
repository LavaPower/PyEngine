import math

__all__ = ["Vec2"]


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.x, self.y

    @coords.setter
    def coords(self, dic):
        self.x = dic[0]
        self.y = dic[1]

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    @length.setter
    def length(self, value):
        length = self.get_length()
        self.x *= value/length
        self.y *= value/length

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        else:
            return Vec2(other - self.x, other - self.y)

    def __isub__(self, other):
        if isinstance(other, Vec2):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __imul__(self, other):
        if isinstance(other, Vec2):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        else:
            return Vec2(self.x // other, self.y // other)

    def __rtruediv__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x // self.x, other.y // self.y)
        else:
            return Vec2(other // self.x, other // self.y)

    def __itruediv__(self, other):
        if isinstance(other, Vec2):
            self.x //= other.x
            self.y //= other.y
        else:
            self.x //= other
            self.y //= other

    def __repr__(self):
        return str(self.coords())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __neg__(self):
        return Vec2(-self.x, -self.y)

