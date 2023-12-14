from __future__ import annotations

import math

from src.objects.ray import Ray
from src.objects.point import Point

from src.constants.constants import RAYS, RAY_X, RAY_Y


class EntityManager:
    def __init__(self, app):
        self.app = app

        self.rays = []

    def create_rays(self):
        for i in range(1):
            p1 = Point(RAY_X, RAY_Y)
            p2 = Point(0, 0)

            self.rays.append(Ray(p1, p2))

    def update_rays():
        for ray in self.rays:
            ...

    def render_rays(self):
        for ray in self.rays:
            ray.render(self.app.window)
