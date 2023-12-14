from __future__ import annotations

import math


class Utility:
    @staticmethod
    def clamp(x, a, b):
        return max(a, min(x, b))

    @staticmethod
    def check_non_zero_component(x, y):
        return abs(x) > 0 or abs(y) > 0

    @staticmethod
    def get_magnitude(x, y):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    @staticmethod
    def get_normalization(x, y):
        magnitude = Utility.get_magnitude(x, y)
        is_non_zero_component = Utility.check_non_zero_component(x, y)

        return 1 / magnitude if is_non_zero_component else 0
