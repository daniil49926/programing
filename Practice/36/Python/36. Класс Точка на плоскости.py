import math
import copy
import enum


@enum.unique
class CoordSystem(enum.Enum):
    Cartesian = enum.auto()
    Polar = enum.auto()


class Point:
    def __init__(self, inp_x=0, inp_y=0, coord_system=CoordSystem.Cartesian):
        if isinstance(inp_x, str):
            a = inp_x.split(",")
            self.x = float(a[0][1:])
            self.y = float(a[1][:-1])
            return

        if coord_system == CoordSystem.Cartesian:
            self.x = inp_x
            self.y = inp_y
            return

        self.x = math.cos(inp_y) * inp_x
        self.y = math.sin(inp_y) * inp_x

    def __eq__(self, other):
        return type(other) == Point and (abs(self.x - other.x) < 1e-10) and (abs(self.y - other.y) < 1e-10)

    def __ne__(self, other):
        return not self == other

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_r(self):
        return math.hypot(self.x, self.y)

    def set_r(self, r):
        phi = self.get_phi()
        self.x = math.cos(phi) * r
        self.y = math.sin(phi) * r

    def get_phi(self):
        return math.atan2(self.y, self.x)

    def set_phi(self, phi):
        r = self.get_r()
        self.x = math.cos(phi) * r
        self.y = math.sin(phi) * r

    def __repr__(self):
        return "Point({},{})".format(
            self.x,
            self.y
        )

    def __str__(self):
        return "({},{})".format(
            self.x,
            self.y
        )


with open('input.txt') as fin:
    original = [Point(p) for p in fin.readline().split(', ')]

simulacrum = copy.deepcopy(original)
for p in simulacrum:
    print(p, end='')
    p.set_x(p.get_x() + 10)
    p.set_phi(p.get_phi() + 180 * math.pi / 180)
    p.set_y(-p.get_y())
    p.set_x(-p.get_x() - 10)
    print(p)

print('\nIt works!\n' if simulacrum == original else '\nIt not works!\n')