from __future__ import annotations

import math
import pygame

from src.objects.ray import Ray
from src.objects.line import Line
from src.objects.point import Point

from src.utilities.utility import Utility

from src.constants.constants import (
    SPEED,
    RAYS,
    RAY_X,
    RAY_Y,
    RADIUS,
    HALF_TAU,
)


class EntityManager:
    def __init__(self, app):
        self.app = app

        self.rays = []
        self.walls = []

    def create_rays(self):
        for ray_index in range(RAYS):
            theta = math.radians(HALF_TAU * (ray_index / RAYS))

            dx = RADIUS * math.cos(theta)
            dy = RADIUS * math.sin(theta)

            p1 = Point(RAY_X, RAY_Y)
            p2 = Point(RAY_X + dx, RAY_Y + dy)

            self.rays.append(Ray(p1, p2))

    def create_walls(self):
        self.walls.append(Line(Point(50, 20), Point(120, 500)))

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

        if keys[pygame.K_s]:
            dy = 1

        return Point(dx, dy)

    def update_rays(self):
        direction = self.get_direction()

        for ray in self.rays:
            normalization = Utility.get_normalization(direction.x, direction.y)

            vx = SPEED * direction.x * normalization
            vy = SPEED * direction.y * normalization

            ray.set_displacement(vx, vy)

            p1 = ray.p1
            p2 = ray.p2

            for wall in self.walls:
                p3 = wall.p1
                p4 = wall.p2

                print(Utility.get_intersection(p1, p2, p3, p4))

    def render_rays(self):
        for ray in self.rays:
            ray.render(self.app.window)

    def render_walls(self):
        for wall in self.walls:
            wall.render(self.app.window)
