from __future__ import annotations

import pygame

from src.constants.constants import WHITE


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def set_position(self, p, x, y):
        p.set_position(x, y)

    def render(self, window):
        pygame.draw.line(window, WHITE, self.p1.get_position(), self.p2.get_position())
