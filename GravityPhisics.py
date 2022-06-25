from math import sqrt
from Object_with_mass import MassObject
from Vector import Vector


G = 6.67 * 10**-11


class GravitiPhisics:
    def __init__(self) -> None:
        pass

    def update_objects(self, objects:set):
        for object in objects:
            object.uptade()
        for object in objects:
            object:MassObject
            f = 0
            objects_a_x = 0
            objects_a_y = 0
            for object2 in objects:
                if(object2 != object):
                    object2:MassObject
                    r_x = (object2.position().x() - object.position().x())*10**7
                    r_y = (object2.position().y() - object.position().y())*10**7
                    if(abs(r_x)<10):
                        f = 1
                    a_g = G * object2.mass()*10**24/(r_x**2 + r_y**2)
                    a_x = sqrt(a_g**2 / (abs(r_y/r_x)**2 + 1)) * (r_x/abs(r_x))
                    a_y = sqrt(a_g**2 / (abs(r_x/r_y)**2 + 1)) * (r_y/abs(r_y))
                    objects_a_x += a_x
                    objects_a_y += a_y
            object.set_acceleration(Vector(objects_a_x, objects_a_y))

