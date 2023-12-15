"""This module provides a vector interface."""

from dataclasses import dataclass


@dataclass
class Point:
    """The point class allows for a callable interface to retrieve coordinate values easily.

    Attributes:
        x (float): The x coordinate of the point.
        y (float): The y coordinate of the point.
    """

    x: float
    y: float

    def set_position(self, x: float, y: float) -> None:
        """Sets the new position of the point.

        Args:
            x (float): The new x coordinate of the point.
            y (float): The new y coordinate of the point.
        """

        self.x = x
        self.y = y

    def get_position(self) -> Point:
        """Returns the position of the current point.

        Returns:
            Point: The current point.
        """

        return (self.x, self.y)
