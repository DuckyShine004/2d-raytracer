from __future__ import annotations

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
    def __init__(self, x, y, color, ray_id):
        super().__init__(x, y, color)

        self.ray_id = ray_id
        self.angle = math.radians(HALF_TAU * (ray_id / RAYS))

    def get_velocity(self, direction):
        normalization = Utility.get_normalization(direction.x, direction.y)

        vx = SPEED * direction.x * normalization
        vy = SPEED * direction.y * normalization

        return Point(vx, vy)

    def set_displacement(self, dx, dy):
        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()

        self.set_position(self.p1, x1 + dx, y1 + dy)
        self.set_position(self.p2, x2 + dx, y2 + dy)

    def update_position(self, position):
        if position:
            self.set_position(self.p2, position.x, position.y)
        else:
            x1, y1 = self.p1.get_position()

            dx = RADIUS * math.cos(self.angle)
            dy = RADIUS * math.sin(self.angle)

            self.set_position(self.p2, x1 + dx, y1 + dy)
