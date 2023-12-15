"""This module aims to handle all events that are related to peripherals.
"""

from __future__ import annotations

import pygame


class EventManager:
    """The event manager will manage all events related to peripherals. For example, quitting an
    application relies on detecting keyboard events.

    Attributes:
        app (App): The main application.
    """

    def __init__(self, app: App) -> None:
        """The event manager constructor.

        Args:
            app (App): The main application.
        """

        self.app = app

    def handle_events(self) -> None:
        """Handle all events that are related to peripherals."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.is_running = False

            self.handle_keyboard_events(event)

    def handle_keyboard_events(self, event: pygame.event.Event) -> None:
        """Handle all keyboard events.

        Args:
            event (pygame.event.Event): The current event.
        """

        if event.type == pygame.KEYDOWN:
            self.handle_keypress(event)

    def handle_keypress(self, event: pygame.event.Event) -> None:
        """Handle key presses.

        Args:
            event (pygame.event.Event): The current event.
        """

        match (event.key):
            case pygame.K_ESCAPE:
                self.app.is_running = False
            case pygame.K_r:
                self.app.entity_manager.create_walls()
