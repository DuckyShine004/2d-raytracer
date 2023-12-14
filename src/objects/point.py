from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)
