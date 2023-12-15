from __future__ import annotations

import pygame


class EventManager:
    def __init__(self, app):
        self.app = app

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.is_running = False

            self.handle_keyboard_events(event)

    def handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.handle_keypress(event)

    def handle_keypress(self, event):
        match (event.key):
            case pygame.K_ESCAPE:
                self.app.is_running = False
            case pygame.K_r:
                self.app.entity_manager.create_walls()
