import pygame
from math import atan2, sin, cos


class Player:

    def __init__(self, screen_width, screen_height):
        self.speed = 1
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.size = 20
        self.x = self.SCREEN_WIDTH / 2
        self.y = self.SCREEN_HEIGHT / 2
        self.play_rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def movement(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dist_x = mouse_x - self.play_rect.centerx
        if -self.speed < dist_x < self.speed:
            dist_x = 0
        dist_y = mouse_y - self.play_rect.centery
        angle = atan2(dist_y, dist_x)
        y_speed = sin(angle) * self.speed
        x_speed = cos(angle) * self.speed
        if -self.speed < dist_x < self.speed:
            x_speed = 0
        if -self.speed < dist_y < self.speed:
            y_speed = 0
        self.x += x_speed
        self.y += y_speed

    def display(self, screen, color):
        self.movement()
        self.play_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, color, self.play_rect)
