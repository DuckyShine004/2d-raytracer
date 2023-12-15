"""This module aims to handle all enitities created within the application."""

from __future__ import annotations

import math
import pygame

from src.objects.ray import Ray
from src.objects.line import Line
from src.objects.point import Point

from src.utilities.utility import Utility

from src.constants.constants import (
    WALLS,
    RAYS,
    RADIUS,
    RAY_X,
    RAY_Y,
    HALF_TAU,
    RAY_COLOR,
    WALL_COLOR,
)


class EntityManager:
    """The entity manager will manager all application entities.

    Attributes:
        app (App): The main application
        rays (list): The array of ray objects.
        walls (list): The array of wall objects.
    """

    def __init__(self, app: App) -> None:
        """The entity manager constructor.

        Args:
            app (App): The main application.
        """

        self.app = app

        self.rays = []
        self.walls = []

    def create_rays(self) -> None:
        """Create rays."""

        for ray_index in range(RAYS):
            theta = math.radians(HALF_TAU * (ray_index / RAYS))

            dx = RADIUS * math.cos(theta)
            dy = RADIUS * math.sin(theta)

            p1 = Point(RAY_X, RAY_Y)
            p2 = Point(RAY_X + dx, RAY_Y + dy)

            self.rays.append(Ray(p1, p2, RAY_COLOR, ray_index))

    def create_walls(self) -> None:
        """Create walls."""

        self.walls.clear()

        for _ in range(WALLS):
            p1 = Utility.get_random_point()
            p2 = Utility.get_random_point()

            self.walls.append(Line(p1, p2, WALL_COLOR))

    def get_direction(self) -> Point:
        """Get the direction of the ray. This depends on the user's key press.

        Returns:
            Point: Returns the direction vector
        """

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

    def update_rays(self) -> None:
        """Update all the rays. This will update the ray's movement, and the collision (if any),
        between the ray object and the walls."""

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

    def render_rays(self) -> None:
        """Render all ray objects."""

        for ray in self.rays:
            ray.render(self.app.window)

    def render_walls(self) -> None:
        """Render all wall objects."""

        for wall in self.walls:
            wall.render(self.app.window)
