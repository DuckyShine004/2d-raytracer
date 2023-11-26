from __future__ import annotations

import pygame

class EventManager:
	def __init__(self, app):
		self.app = app

	def handle_events(self):
		for event in pygame.event.get():
			self.handle_keyboard_events(event)

	def handle_keyboard_events(self, event):
		self.handle_quit_event(event)

	def handle_quit_event(self, event):
		if event.type == pygame.QUIT:
			self.app.is_running = False

