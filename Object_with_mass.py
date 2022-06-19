


class MassObject:
    def __init__(self, name:str, mass:int, position:tuple, speed:int = 0, acceleration:int = 0) -> None:
        self._name = name
        self._mass = mass
        self._speed = speed
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

    def set_name(self, new_name:str):
        self._name = new_name

    def set_mass(self, new_mass:int):
        self._mass = new_mass

    def set_acceleration(self, new_acceleration:int):
        self._acceleration = new_acceleration

    def set_speed(self, new_speed:int):
        self._speed = new_speed

    def set_position(self, new_position:int):
        self._position = new_position