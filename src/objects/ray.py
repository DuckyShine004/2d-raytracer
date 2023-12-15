"""The ray module is an object."""

import math

from src.objects.line import Line
from src.objects.point import Point

from src.utilities.utility import Utility

from src.constants.constants import (
    SPEED,
    RAYS,
    RADIUS,
    HALF_TAU,
)


class Ray(Line):
    """The ray class defines what a ray is.

    Attributes:
        angle (float): The ray's angle.
        ray_id (int): The ray's id.
    """

    def __init__(
        self, x: float, y: float, color: Tuple[float, float, float], ray_id: int
    ) -> None:
        """The Ray object constructor.

        Args:
            x (float): The x coordinate of the ray.
            y (float): The y coordinate of the ray.
            color (Tuple[float, float, float]): The color of the ray.
            ray_id (int): The ray's id.
        """

        super().__init__(x, y, color)

        self.ray_id = ray_id
        self.angle = math.radians(HALF_TAU * (ray_id / RAYS))

    def get_velocity(self, direction: Point) -> Point:
        """Calculates the velocity of the ray, adn returns the velocity vector.

        Args:
            direction (Point): The directional vector of the ray.

        Returns:
            Point: The velocity vector of the ray.
        """

        normalization = Utility.get_normalization(direction.x, direction.y)

        vx = SPEED * direction.x * normalization
        vy = SPEED * direction.y * normalization

        return Point(vx, vy)

    def set_displacement(self, dx: float, dy: float) -> None:
        """Displaces the current ray by the queried amount.

        Args:
            dx (float): The horizontal displacement value.
            dy (float): The vertical displacement value.
        """

        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()

        self.set_position(self.p1, x1 + dx, y1 + dy)
        self.set_position(self.p2, x2 + dx, y2 + dy)

    def update_position(self, position: Point) -> None:
        """Updates the position of the current ray. If there is no intersection, we recalculate the
        original ray length.

        Args:
            position (Point): The new position of the point.
        """

        if position:
            self.set_position(self.p2, position.x, position.y)
        else:
            x1, y1 = self.p1.get_position()

            dx = RADIUS * math.cos(self.angle)
            dy = RADIUS * math.sin(self.angle)

            self.set_position(self.p2, x1 + dx, y1 + dy)
