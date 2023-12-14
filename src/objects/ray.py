from __future__ import annotations

import pygame

from src.objects.point import Point

from src.constants.constants import WHITE


class Ray:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def set_displacement(self, dx, dy):
        x1, y1 = self.p1.get_pos()
        x2, y2 = self.p2.get_pos()

        self.set_pos(self.p1, x1 + dx, y1 + dy)
        self.set_pos(self.p2, x2 + dx, y2 + dy)

    def set_pos(self, p, x, y):
        p.set_pos(x, y)

    def render(self, window):
        pygame.draw.line(window, WHITE, self.p1.get_pos(), self.p2.get_pos())
