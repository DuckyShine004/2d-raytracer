from __future__ import annotations

import math
import pygame

from src.objects.ray import Ray
from src.objects.line import Line
from src.objects.point import Point

from src.utilities.utility import Utility

from src.constants.constants import (
    WALLS,
    SPEED,
    RAYS,
    RADIUS,
    RAY_X,
    RAY_Y,
    RADIUS,
    HALF_TAU,
    RAY_COLOR,
    WALL_COLOR,
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

            self.rays.append(Ray(p1, p2, RAY_COLOR, ray_index))

    def create_walls(self):
        self.walls.clear()

        for _ in range(WALLS):
            p1 = Utility.get_random_point()
            p2 = Utility.get_random_point()

            self.walls.append(Line(p1, p2, WALL_COLOR))

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
            velocity = ray.get_velocity(direction)

            closest = RADIUS
            closest_point = None

            ray.set_displacement(velocity.x, velocity.y)

            for wall in self.walls:
                p1 = ray.p1
                p2 = ray.p2
                p3 = wall.p1
                p4 = wall.p2

                intersection = Utility.get_intersection(p1, p2, p3, p4)

                if intersection:
                    distance = Utility.get_distance(p1, intersection)

                    if distance < closest:
                        closest = distance
                        closest_point = intersection

            ray.update_position(closest_point)

    def render_rays(self):
        for ray in self.rays:
            ray.render(self.app.window)

    def render_walls(self):
        for wall in self.walls:
            wall.render(self.app.window)
