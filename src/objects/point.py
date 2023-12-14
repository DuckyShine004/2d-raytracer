from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)
