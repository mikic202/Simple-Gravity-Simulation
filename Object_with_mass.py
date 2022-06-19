


class MassObject:
    def __init__(self, mass:int, position:tuple, speed:int = 0, acceleration:int = 0) -> None:
        self._mass = mass
        self._speed = position
        self._acceleration = acceleration
        self._position = position