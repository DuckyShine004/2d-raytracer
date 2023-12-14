from __future__ import annotations

import math

from src.objects.ray import Ray
from src.objects.point import Point

from src.constants.constants import RAYS, RAY_X, RAY_Y, RADIUS, HALF_TAU


class EntityManager:
    def __init__(self, app):
        self.app = app

        self.rays = []

    def create_rays(self):
        p1 = Point(RAY_X, RAY_Y)

        for ray_index in range(RAYS):
            theta = math.radians(HALF_TAU * (ray_index / RAYS))

            dx = RADIUS * math.cos(theta)
            dy = RADIUS * math.sin(theta)

            p2 = Point(RAY_X + dx, RAY_Y + dy)

            self.rays.append(Ray(p1, p2))

    def update_rays(self):
        for ray in self.rays:
            ...

    def render_rays(self):
        for ray in self.rays:
            ray.render(self.app.window)
