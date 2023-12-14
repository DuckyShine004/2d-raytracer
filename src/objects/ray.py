from __future__ import annotations

import pygame

from src.objects.line import Line


class Ray(Line):
    def set_displacement(self, dx, dy):
        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()

        self.set_position(self.p1, x1 + dx, y1 + dy)
        self.set_position(self.p2, x2 + dx, y2 + dy)
