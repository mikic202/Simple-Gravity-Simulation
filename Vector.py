

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

    def set_x(self, new_x_val):
        self._x = new_x_val

    def set_y(self, new_y_val):
        self._y = new_y_val

    def set_z(self, new_z_val):
        self._z = new_z_val

    def __str__(self) -> str:
        return f'{self._x:.4}    {self._y:.4}'
