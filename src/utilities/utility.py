from __future__ import annotations

import math

from src.objects.point import Point


class Utility:
    @staticmethod
    def clamp(x, a, b):
        return max(a, min(x, b))

    @staticmethod
    def check_non_zero_component(x, y):
        return abs(x) > 0 or abs(y) > 0

    @staticmethod
    def get_magnitude(x, y):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    @staticmethod
    def get_normalization(x, y):
        magnitude = Utility.get_magnitude(x, y)
        is_non_zero_component = Utility.check_non_zero_component(x, y)

        return 1 / magnitude if is_non_zero_component else 0

    @staticmethod
    def get_determinant(a, b, c, d):
        return (a * d) - (b * c)

    @staticmethod
    def get_determinants(x1, x2, x3, x4, y1, y2, y3, y4):
        a = Utility.get_determinant(x1, y1, x2, y2)
        b = Utility.get_determinant(x1, 1, x2, 1)
        c = Utility.get_determinant(x3, y3, x4, y4)
        d = Utility.get_determinant(x3, 1, x4, 1)
        e = Utility.get_determinant(y1, 1, y2, 1)
        f = Utility.get_determinant(y3, 1, y4, 1)

        return [a, b, c, d, e, f]

    @staticmethod
    def get_intersection_point(determinants):
        a, b, c, d, e, f = determinants

        px = Utility.get_determinant(a, b, c, d) / Utility.get_determinant(b, e, d, f)
        py = Utility.get_determinant(a, e, c, f) / Utility.get_determinant(b, e, d, f)

        return Point(px, py)

    @staticmethod
    def get_intersection(p1, p2, p3, p4):
        x1, y1 = p1.get_position()
        x2, y2 = p2.get_position()
        x3, y3 = p3.get_position()
        x4, y4 = p4.get_position()

        determinants = Utility.get_determinants(x1, x2, x3, x4, y1, y2, y3, y4)

        return Utility.get_intersection_point(determinants)
