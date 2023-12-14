from __future__ import annotations

import math
import pygame

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

    def get_direction(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx = -1

        if keys[pygame.K_d]:
            dx = 1

        if keys[pygame.K_w]:
            dy = -1

        if key[pygame.K_s]:
            dy = 1

        return Point(dx, dy)

    def update_rays(self):
        direction = self.get_direction()

        for ray in self.rays:
            ...

    def render_rays(self):
        for ray in self.rays:
            ray.render(self.app.window)
