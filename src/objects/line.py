from __future__ import annotations

from dataclasses import dataclass

import pygame

from src.objects.point import Point

from src.constants.constants import WHITE


@dataclass
class Line:
    p1: Point
    p2: Point

    def set_position(self, p, x, y):
        p.set_position(x, y)

    def render(self, window):
        pygame.draw.line(window, WHITE, self.p1.get_position(), self.p2.get_position())
