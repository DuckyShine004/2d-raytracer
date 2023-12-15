from __future__ import annotations

import pygame

from src.constants.constants import WHITE


class Line:
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def set_position(self, p, x, y):
        p.set_position(x, y)

    def render(self, window):
        p1 = self.p1.get_position()
        p2 = self.p2.get_position()

        pygame.draw.line(window, self.color, p1, p2)
