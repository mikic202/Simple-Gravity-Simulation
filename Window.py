import sys
import pygame
from GravityPhisics import GravitiPhisics
from Object_with_mass import MassObject
from Vector import Vector

pygame.init()

FONT = pygame.font.Font('freesansbold.ttf', 13)
WHITE = (255, 255, 255)

start_width = 1000
start_height = 800
# first_object_pos = Vector(0, 0)
# second_object_pos = Vector(400, 693)
# first_object_v = Vector(0.05, -0.029)
# second_object_v = Vector(-0.05, -0.029)
# third_object_pos = Vector(800, 1)
# third_object_v = Vector(0.029, 0.05)

first_object_pos = Vector(200, 100)
second_object_pos = Vector(800, 800)
first_object_v = Vector(1.4, 0)
second_object_v = Vector(-1, 0)
third_object_pos = Vector(400, 400)
third_object_v = Vector(0, 0)


class Window:
    def __init__(self) -> None:
        self._WIN = pygame.display.set_mode((start_width, start_height))
        self._objects = {MassObject("a", 1.5, first_object_pos, first_object_v), MassObject("b", .00001, second_object_pos, second_object_v), MassObject("c", 1000, third_object_pos, third_object_v)}
        self._phisics = GravitiPhisics()
        self._start()

    def _start(self):
        while True:
            self._phisics.update_objects(self._objects)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for object in self._objects:
                pygame.draw.circle(self._WIN, (255, 255, 255), [object.position().x(), object.position().y()], 20)
            self._display_parameters()
            pygame.display.update()
            self._WIN.fill((0, 0, 0))

    def _display_parameters(self):
        pixels_drawn = 0
        for object in self._objects:
            name_text = FONT.render(f'Name: {object.name()}', True, WHITE)
            self._WIN.blit(name_text, (start_width - 200, pixels_drawn))
            mass_text = FONT.render(f'Mass: {object.mass()}', True, WHITE)
            self._WIN.blit(mass_text, (start_width - 100, pixels_drawn))
            pixels_drawn += 13
            position_text = FONT.render(f'Position: {object.position()}', True, WHITE)
            self._WIN.blit(position_text, (start_width - 200, pixels_drawn))
            pixels_drawn += 13



win = Window()