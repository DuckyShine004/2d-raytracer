import os
import pygame

from src.app.app import App


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()

    app = App()

    app.run()
