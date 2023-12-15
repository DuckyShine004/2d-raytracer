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
    def check_valid_coefficients(coefficients):
        t, u = coefficients

        if not (t and u):
            return False

        return 0 < t < 1 and u > 0

    @staticmethod
    def get_magnitude(x, y):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    @staticmethod
    def get_distance(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y

        return Utility.get_magnitude(dx, dy)

    @staticmethod
    def get_normalization(x, y):
        magnitude = Utility.get_magnitude(x, y)

        return 1 / magnitude if Utility.check_non_zero_component(x, y) else 0

    @staticmethod
    def get_determinant(a, b, c, d):
        return (a * d) - (b * c)

    @staticmethod
    def get_determinants(positions):
        x1, x2, x3, x4, y1, y2, y3, y4 = positions

        a = x1 - x3
        b = x3 - x4
        c = y1 - y3
        d = y3 - y4
        e = x1 - x2
        f = y1 - y2

        return [a, b, c, d, e, f]

    @staticmethod
    def get_bezier_coefficients(determinants):
        a, b, c, d, e, f = determinants

        numerator_t = Utility.get_determinant(a, b, c, d)
        numerator_u = Utility.get_determinant(a, e, c, f)

        denominator = Utility.get_determinant(e, b, f, d)

        if denominator == 0:
            return None, None

        t = numerator_t / denominator
        u = numerator_u / denominator

        return t, u

    @staticmethod
    def get_intersection_point(coefficients, x1, x2, y1, y2):
        print(coefficients[0], Point(x2, y2))

        if not Utility.check_valid_coefficients(coefficients):
            return None

        t, u = coefficients

        t = Utility.clamp(t, 0, 1)
        u = Utility.clamp(u, 0, 1)

        px = x1 + t * (x2 - x1)
        py = y1 + t * (y2 - y1)

        return Point(px, py)

    @staticmethod
    def get_intersection(p1, p2, p3, p4):
        x3, y3 = p1.get_position()
        x4, y4 = p2.get_position()
        x1, y1 = p3.get_position()
        x2, y2 = p4.get_position()

        positions = [x1, x2, x3, x4, y1, y2, y3, y4]

        determinants = Utility.get_determinants(positions)
        coefficients = Utility.get_bezier_coefficients(determinants)

        return Utility.get_intersection_point(coefficients, x1, x2, y1, y2)
