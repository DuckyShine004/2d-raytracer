"""This module contains the main code needed to run the application."""
import os
import pygame

from src.app.app import App


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()

    app = App()

    app.initialize()

    app.run()
