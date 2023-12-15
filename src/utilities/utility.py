"""The utility module aims to provide an interface for useful helper functions."""

from typing import List, Tuple

import math
import random

from src.objects.point import Point

from src.constants.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class Utility:
    """The utility class provides a callable interface for helper functions."""

    @staticmethod
    def check_non_zero_component(x: float, y: float) -> bool:
        """Checks if both of the vector components are non zero.

        Args:
            x (float): The x coordinate of the component.
            y (float): The y coordinate of the component.

        Returns:
            bool: The result of validating whether the components are non zero.
        """

        return abs(x) > 0 or abs(y) > 0

    @staticmethod
    def check_valid_coefficients(coefficients: Tuple[float, float]) -> bool:
        """Checks whether the linear Bezier coefficients are valid.

        Args:
            coefficients (Tuple[float, float]): The linear Bezier coefficients.

        Returns:
            bool: The result of validating whether the coefficients are valid.
        """

        t, u = coefficients

        if not (t and u):
            return False

        return 0 < t < 1 and u > 0

    @staticmethod
    def get_random_point() -> Point:
        """Creates a random point and returns it.

        Returns:
            Point: Returns a random point.
        """

        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)

        return Point(x, y)

    @staticmethod
    def get_magnitude(x: float, y: float) -> float:
        """Calculates the magnitude of the vector and returns it.

        Args:
            x (float): The x component of the vector.
            y (float): The y component of the vector.

        Returns:
            float: The magnitude of the vector.
        """

        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    @staticmethod
    def get_distance(p1: Point, p2: Point) -> float:
        """Calculates the Euclidean distance between two points.

        Args:
            p1 (Point): Point 1.
            p2 (Point): Point 2.

        Returns:
            float: The distance between the two points.
        """

        dx = p1.x - p2.x
        dy = p1.y - p2.y

        return Utility.get_magnitude(dx, dy)

    @staticmethod
    def get_normalization(x: float, y: float) -> float:
        """Calculates the unit vector and returns it.

        Args:
            x (float): The x component of the vector.
            y (float): The y component of the vector.

        Returns:
            float: The unit vector (normalized vector).
        """

        magnitude = Utility.get_magnitude(x, y)

        return 1 / magnitude if Utility.check_non_zero_component(x, y) else 0

    @staticmethod
    def get_determinant(a: float, b: float, c: float, d: float) -> float:
        """Calculates the determinant for the values, a, b, c, and d.

        Args:
            a (float): Value 1.
            b (float): Value 2.
            c (float): Value 3.
            d (float): Value 4.

        Returns:
            float: The determinant value.
        """

        return (a * d) - (b * c)

    @staticmethod
    def get_determinants(positions: List[float]) -> List[float]:
        """Pre-calculates the determinant values and returns it.

        Args:
            positions (List[float]): The list of all positions.

        Returns:
            List[float]: A list of the pre-calculated determinant values.
        """

        x1, x2, x3, x4, y1, y2, y3, y4 = positions

        a = x1 - x3
        b = x3 - x4
        c = y1 - y3
        d = y3 - y4
        e = x1 - x2
        f = y1 - y2

        return [a, b, c, d, e, f]

    @staticmethod
    def get_bezier_coefficients(determinants: List[float]) -> Tuple[float, float]:
        """Calculates the Bezier coefficients and returns it.

        Args:
            determinants (List[float]): The list of all determinants.

        Returns:
            Tuple[float, float]: the Bezier coefficients.
        """

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
    def get_intersection_point(
        coefficients: Tuple[float, float], p1: Point, p2: Point
    ) -> Point:
        """Returns the point of intersection if the intersection is valid.

        Args:
            coefficients (Tuple[float, float]): The Bezier coefficients.
            p1 (Point): Point 1.
            p2 (Point): Point 2.

        Returns:
            Point: Returns the point of intersection.
        """

        x1, y1 = p1.get_position()
        x2, y2 = p2.get_position()

        if not Utility.check_valid_coefficients(coefficients):
            return None

        t = coefficients[0]

        px = x1 + t * (x2 - x1)
        py = y1 + t * (y2 - y1)

        return Point(px, py)

    @staticmethod
    def get_intersection(p1: Point, p2: Point, p3: Point, p4: Point) -> Point:
        """Gets the intersection between the two line segments. p1 and p2 belongs to the ray line
        segments, and p3 and p4 belongs to the wall line segment.

        Args:
            p1 (Point): Point 1.
            p2 (Point): Point 2.
            p3 (Point): Point 2.
            p4 (Point): Point 2.

        Returns:
            Point: Returns the point of intersection.
        """

        x3, y3 = p1.get_position()
        x4, y4 = p2.get_position()
        x1, y1 = p3.get_position()
        x2, y2 = p4.get_position()

        positions = [x1, x2, x3, x4, y1, y2, y3, y4]

        determinants = Utility.get_determinants(positions)
        coefficients = Utility.get_bezier_coefficients(determinants)

        return Utility.get_intersection_point(coefficients, p3, p4)
