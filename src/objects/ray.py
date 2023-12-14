from __future__ import annotations

import math
import pygame

from src.objects.line import Line

from src.constants.constants import (
    SPEED,
    RAYS,
    RADIUS,
    HALF_TAU,
)


class Ray(Line):
    def __init__(self, x, y, ray_id):
        super().__init__(x, y)

        self.ray_id = ray_id

    def set_displacement(self, dx, dy):
        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()

        self.set_position(self.p1, x1 + dx, y1 + dy)
        self.set_position(self.p2, x2 + dx, y2 + dy)

    def update_position(self, position):
        print(position, self.p2, self.ray_id)
        if position:
            self.set_position(self.p2, position.x, position.y)
        else:
            x1, y1 = self.p1.get_position()

            theta = math.radians(HALF_TAU * (self.ray_id / RAYS))

            dx = RADIUS * math.cos(theta)
            dy = RADIUS * math.sin(theta)

            self.set_position(self.p2, x1 + dx, y1 + dy)
