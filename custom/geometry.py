from manimlib import VGroup
from manimlib import Dot
from manimlib import Tex
from manimlib import Polygon
from manimlib import Line
from manimlib import angle_of_vector
from manimlib import midpoint
from manimlib.constants import *


# Dot with a mark label (Dot Extended)
class DotX(VGroup):
    def __init__(self,
                 point: np.ndarray = ORIGIN,
                 mark_letter: str = "P",
                 point_config=None,
                 mark_config=None,
                 mark_pos=UL,
                 **kwargs
                 ):
        # Dot
        if point_config:
            self.dot = Dot(point, **point_config)
        else:
            self.dot = Dot(point)

        # Mark letter
        if mark_config:
            self.mark = Tex(mark_letter, **mark_config)
        else:
            self.mark = Tex(mark_letter)

        self.mark.next_to(self.dot, mark_pos)

        super().__init__(self.dot, self.mark, **kwargs)

    def get_point(self):
        return self.dot.get_center()


# Triangle with dots and marks (Triangle Extended)
class TriangleX(VGroup):
    def __init__(self, *dotxes: DotX, triangle_config=None, **kwargs):
        # DotXes
        self.dotxes = dotxes

        # Triangle
        points = []
        for dotx in dotxes:
            points.append(dotx.dot.get_center())

        self.triangle_config = triangle_config
        if triangle_config:
            self.tri = Polygon(*points, **triangle_config)
        else:
            self.tri = Polygon(*points)

        super().__init__(*self.dotxes, self.tri, **kwargs)

    def set_color_for_marks(self, color):
        for dotx in self.dotxes:
            dotx.mark.set_color(color)
        return self

    def copy(self):
        copied = super().copy()
        dotxes = []

        for mobject in copied:
            if isinstance(mobject, DotX):
                dotxes.append(mobject)
            elif isinstance(mobject, Polygon):
                copied.tri = mobject

        copied.dotxes = tuple(dotxes)
        return copied


# Draw a tick of a line defined by two points
def get_tick(point_a: np.ndarray, point_b: np.ndarray, width: float = 0.2, color=WHITE) -> Line:
    vector = point_b - point_a
    line_angle = angle_of_vector(vector)
    tick_angle = PI / 2 + line_angle
    mid_point = midpoint(point_a, point_b)
    half_width = width / 2

    tick = Line(half_width * LEFT, half_width * RIGHT, color=color)
    tick.move_to(mid_point)
    tick.rotate(tick_angle)
    return tick


# Draw double tick of a line defined by two points
def get_double_tick(point_a: np.ndarray, point_b: np.ndarray, width: float = 0.2, color=WHITE) -> VGroup:
    buff = 0.07
    unit_vector_ab = get_unit_vector_on_direction(point_b - point_a)

    tick1 = get_tick(point_a, point_b, width=width, color=color)
    tick1.shift(unit_vector_ab * buff)
    tick2 = get_tick(point_a, point_b, width=width, color=color)
    tick2.shift(-unit_vector_ab * buff)

    return VGroup(tick1, tick2)


def get_unit_vector_on_direction(vector: np.ndarray) -> np.ndarray:
    angle = angle_of_vector(vector)
    return np.array([np.cos(angle), np.sin(angle), 0])


# Get the vertical point coord of C to line AB
def get_vertical_point(point_a: np.ndarray, point_b: np.ndarray, point_c: np.ndarray) -> np.ndarray:
    x1 = point_a[0]
    y1 = point_a[1]
    x2 = point_b[0]
    y2 = point_b[1]
    x0 = point_c[0]
    y0 = point_c[1]

    # Brute-force calculation
    x = ((x0 * (x2 - x1) ** 2 + x1 * (y2 - y1) ** 2 + (y0 - y1) * (x2 - x1) * (y2 - y1)) /
         ((y2 - y1) ** 2 + (x2 - x1) ** 2))
    y = (y2 - y1) / (x2 - x1) * (x - x1) + y1

    return np.array([x, y, 0])


# Get the angle value of 3 given points (point_b as the vertex)
def get_angle_of_3_points(point_a: np.ndarray, point_b: np.ndarray, point_c: np.ndarray):
    vector_ba = point_a - point_b
    vector_bc = point_c - point_b
    x1 = vector_ba[0]
    y1 = vector_ba[1]
    x2 = vector_bc[0]
    y2 = vector_bc[1]

    cos_theta = (x1 * x2 + y1 * y2) / (np.sqrt(x1 ** 2 + y1 ** 2) * np.sqrt(x2 ** 2 + y2 ** 2))
    return np.arccos(cos_theta)

