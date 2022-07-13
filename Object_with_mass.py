from Vector import Vector


TIME = 4


class MassObject:
    def __init__(self, name:str, mass:int, position:Vector, radius:int, speed:Vector = 0, acceleration:Vector = 0) -> None:
        self._name = name
        self._radius = radius
        self._mass = mass
        if(speed == 0):
            speed = Vector()
        self._speed = speed
        if(acceleration == 0):
            acceleration = Vector()
        self._acceleration = acceleration
        self._position = position

    def name(self):
        return self._name

    def mass(self):
        return self._mass

    def speed(self):
        return self._speed

    def acceleration(self):
        return self._acceleration

    def position(self):
        return self._position

    def radius(self):
        return self._radius

    def set_name(self, new_name:str):
        self._name = new_name

    def set_mass(self, new_mass:int):
        self._mass = new_mass

    def set_acceleration(self, new_acceleration:Vector):
        self._acceleration = new_acceleration

    def set_speed(self, new_speed:Vector):
        self._speed = new_speed

    def set_position(self, new_position:Vector):
        self._position = new_position

    def set_radius(self, new_radius:int):
        self._radius = new_radius

    def uptade(self):
        self._position.set_x(self._position.x() + self._speed.x()*TIME + 0.5*self._acceleration.x()*TIME**2)
        self._position.set_y(self._position.y() + self._speed.y()*TIME + 0.5*self._acceleration.y()*TIME**2)
        self._speed.set_x(self.speed().x() + self.acceleration().x()*TIME)
        self._speed.set_y(self.speed().y() + self.acceleration().y()*TIME)