from __future__ import annotations

import pygame

from managers.event_manager import EventManager
from managers.entity_manager import EntityManager

from src.constants.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_COLOR,
)


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.is_running = True

        self.event_manager = EventManager(self)
        self.entity_manager = EntityManager(self)

        # Test
        self.entity_manager.create_rays()

    def run(self):
        while self.is_running:
            self.event_manager.handle_events()
            self.window.fill(WINDOW_COLOR)

            self.entity_manager.render_rays()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    app = App()

    app.run()
