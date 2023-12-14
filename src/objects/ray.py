from __future__ import annotations

import pygame

from src.objects.point import Point

from src.constants.constants import WHITE


class Ray:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def set_pos(self, p, x, y):
        p.set_pos(x, y)

    def render(self, window):
        pygame.draw.line(window, WHITE, self.p1.get_pos(), self.p2.get_pos())
