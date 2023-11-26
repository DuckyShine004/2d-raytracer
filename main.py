from __future__ import annotations

import pygame

from managers.event_manager import EventManager
from src.constants.application_constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_COLOR


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.is_running = True

        self.event_manager = EventManager(self)

    def run(self):
        while self.is_running:
            self.event_manager.handle_events()
            self.window.fill(WINDOW_COLOR)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    app = App()

    app.run()
