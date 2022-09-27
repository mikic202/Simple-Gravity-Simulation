from pickle import TRUE
import sys
import pygame
from GravityPhisics import GravitiPhisics
from Object_with_mass import MassObject
from Vector import Vector
import time

pygame.init()

FONT_SIZE = 13
FONT = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
WHITE = (255, 255, 255)

start_width = 1000
start_height = 1000
# first_object_pos = Vector(0, 0)
# second_object_pos = Vector(400, 693)
# first_object_v = Vector(0.05, -0.029)
# second_object_v = Vector(-0.05, -0.029)
# third_object_pos = Vector(800, 1)
# third_object_v = Vector(0.029, 0.05)

first_object_pos = Vector(400, 250)
second_object_pos = Vector(400, 800)
first_object_v = Vector(0.93, 0.0)
second_object_v = Vector(-.5745, 0.0)
third_object_pos = Vector(400, 400)
third_object_v = Vector(0.0, 0.0)

#, MassObject("b", .00001, second_object_pos, second_object_v)


class Window:
    def __init__(self) -> None:
        self._WIN = pygame.display.set_mode((start_width, start_height))
        self._objects = [MassObject("a", 3.28*10**23, first_object_pos, 10, first_object_v), MassObject("c", 1.98*10**30, third_object_pos, 15, third_object_v), MassObject("b", .00001, second_object_pos, 5, second_object_v)]
        self._phisics = GravitiPhisics()
        self._start()

    def _start(self):
        while True:
            self._phisics.update_objects(self._objects)
            self._check_quit()
            self._check_pause()
            self._draw_objects()
            self._display_parameters()
            pygame.display.update()
            self._WIN.fill((0, 0, 0))

    def _display_parameters(self):
        pixels_drawn = 0
        mass_text = FONT.render(f'Mass [kg]', True, WHITE)
        self._WIN.blit(mass_text, (start_width - 300, pixels_drawn))
        position_text = FONT.render(f'Position [m * 10^10]', True, WHITE)
        self._WIN.blit(position_text, (start_width - 175, pixels_drawn))
        pixels_drawn += FONT_SIZE
        speed_text = FONT.render(f'Speed  [m/s * 10^4]', True, WHITE)
        self._WIN.blit(speed_text, (start_width - 300, pixels_drawn))
        acceleration_text = FONT.render(f'Acceleration [km/s^2]', True, WHITE)
        self._WIN.blit(acceleration_text, (start_width - 175, pixels_drawn))
        pixels_drawn += FONT_SIZE + 8
        for object in self._objects:
            name_text = FONT.render(f'Name: {object.name()}', True, WHITE)
            self._WIN.blit(name_text, (start_width - 250, pixels_drawn))
            mass_text = FONT.render(f'Mass: {object.mass()}', True, WHITE)
            self._WIN.blit(mass_text, (start_width - 125, pixels_drawn))
            pixels_drawn += FONT_SIZE
            position_text = FONT.render(f'Position: {object.position()}', True, WHITE)
            self._WIN.blit(position_text, (start_width - 250, pixels_drawn))
            pixels_drawn += FONT_SIZE
            speed_text = FONT.render(f'Speed: {object.speed()}', True, WHITE)
            self._WIN.blit(speed_text, (start_width - 250, pixels_drawn))
            pixels_drawn += FONT_SIZE
            acceleration_text = FONT.render(f'Acceleration: {object.acceleration()}', True, WHITE)
            self._WIN.blit(acceleration_text, (start_width - 250, pixels_drawn))
            pixels_drawn += FONT_SIZE + 8

    def _draw_objects(self):
        for object in self._objects:
            pygame.draw.circle(self._WIN, (255, 255, 255), [object.position().x(), object.position().y()], object.radius())
            name_text = FONT.render(f'{object.name()}', True, WHITE)
            self._WIN.blit(name_text, [object.position().x(), object.position().y() + object.radius()])

    def _check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _check_pause(self):
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_SPACE]:
            needs_to_stop = True
            time.sleep(2)
            while needs_to_stop:
                self._check_quit()
                keys_press = pygame.key.get_pressed()
                if keys_press[pygame.K_SPACE]:
                    needs_to_stop = False
            time.sleep(.5)


if __name__ == "__main__":
    win = Window()