

class Vector:
    def __init__(self, x_val=0, y_val=0, z_val=0) -> None:
        self._x = x_val
        self._y = y_val
        self._z = z_val

    def x(self):
        return self._x

    def y(self):
        return self._y

    def z(self):
        return self._z