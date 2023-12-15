"""This module contains the main application."""

import pygame

from managers.event_manager import EventManager
from managers.entity_manager import EntityManager

from src.constants.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_COLOR,
    FRAME_RATE,
)


class App:
    """The app class contains the code necessary to run the application.

    Attributes:
        entity_manager (EntityManager): The entity manager.
        event_manager (EventManager): The event manager.
        is_running (bool): Is the application running.
        window (pygame.Surface): The surface to draw objects onto.
    """

    def __init__(self) -> None:
        """The app object constructor."""

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.is_running = True

        self.event_manager = EventManager(self)
        self.entity_manager = EntityManager(self)

    def initialize(self) -> None:
        """Initializes important things before running the application."""

        self.entity_manager.create_rays()
        self.entity_manager.create_walls()

    def run(self) -> None:
        """Runs the app."""

        while self.is_running:
            self.event_manager.handle_events()
            self.window.fill(WINDOW_COLOR)

            self.entity_manager.update_rays()

            self.entity_manager.render_rays()
            self.entity_manager.render_walls()

            pygame.display.flip()
            pygame.time.Clock().tick(FRAME_RATE)

        pygame.quit()
