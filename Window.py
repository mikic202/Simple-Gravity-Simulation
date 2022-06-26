import sys
import pygame
from GravityPhisics import GravitiPhisics
from Object_with_mass import MassObject
from Vector import Vector


start_width = 800
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
                print(object.position().y())
                print("\n")
                pygame.draw.circle(self._WIN, (255, 255, 255), [object.position().x(), object.position().y()], 20)
            pygame.display.update()
            self._WIN.fill((0, 0, 0))



win = Window()