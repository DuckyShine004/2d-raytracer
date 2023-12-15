"""This module contains essential application constants.

Attributes:
    BLUE (Tuple[float, float, float]): The color blue.
    FRAME_RATE (int): The frame rate.
    GREEN (Tuple[float, float, float]): The color green.
    HALF_TAU (int): 360 degrees.
    RADIUS (int): The radius of the ray.
    RAY_COLOR (Tuple[float, float, float]): The ray's color.
    RAY_X (int): The initial x coordinate of the ray.
    RAY_Y (int): The initial y coordinate of the ray.
    RAYS (int): The number of rays to be displayed or casted.
    RED (Tuple[float, float, float]): The color red.
    SPEED (int): The speed of the ray.
    WALL_COLOR (Tuple[float, float, float]): The color of the walls.
    WALLS (int): The number of walls to be displayed.
    WHITE (Tuple[float, float, float]): The color white.
    WINDOW_COLOR (Tuple[float, float, float]): The display color.
    WINDOW_HEIGHT (int): The height of the window.
    WINDOW_WIDTH (int): The width of the window.
"""

# Window and GUI
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_COLOR = (0, 0, 0)
FRAME_RATE = 60

# Objects
WALLS = 4
SPEED = 10
RAYS = 150
RAY_X = WINDOW_WIDTH // 2
RAY_Y = WINDOW_HEIGHT // 2

# Circle
RADIUS = 10000
HALF_TAU = 360

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Default line colors
RAY_COLOR = RED
WALL_COLOR = WHITE
