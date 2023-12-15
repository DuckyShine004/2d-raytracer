"""This module provides a way to create a Line object."""

from typing import Tuple

import pygame

from src.objects.point import Point


class Line:
    """The Line class is a parent class. It is a 2d line in Euclidean space.

    Attributes:
        p1 (Point): Point 1.
        p2 (Point): Point 2.
        color (TYPE): The color of the line.
    """

    def __init__(self, p1: Point, p2: Point, color: Tuple[float, float, float]) -> None:
        """The Line object constructor.

        Args:
            p1 (Point): Point 1.
            p2 (Point): Point 2.
            color (Tuple[float, float, float]): The color of the line.
        """

        self.p1 = p1
        self.p2 = p2
        self.color = color

    def set_position(self, p: Point, x: float, y: float) -> None:
        """Sets the position of a point on the line segment.

        Args:
            p (TYPE): The point to be set.
            x (TYPE): The new x coordinate.
            y (TYPE): The new y coordinate.
        """

        p.set_position(x, y)

    def render(self, window: pygame.Surface) -> None:
        """Renders the line object onto the screen.

        Args:
            window (pygame.Surface): The surface which the line will be rendered onto.
        """

        p1 = self.p1.get_position()
        p2 = self.p2.get_position()

        pygame.draw.line(window, self.color, p1, p2)
