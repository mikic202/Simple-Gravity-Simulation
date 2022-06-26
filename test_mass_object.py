from Object_with_mass import TIME, MassObject
from Vector import Vector


def test_init_with_all_param():
    object = MassObject("nam", 10, Vector(1, 2, 3), Vector(4, 5), Vector(8, 7))

    assert object.name() == "nam"
    assert object.mass() == 10
    assert object.position().x() == 1
    assert object.speed().x() == 4
    assert object.acceleration().x() == 8


def test_init_only_needed_param():
    object = MassObject("nam", 10, Vector(1, 2, 3))

    assert object.name() == "nam"
    assert object.mass() == 10
    assert object.position().x() == 1
    assert object.speed().x() == 0
    assert object.acceleration().x() == 0


def test_set_name():
    object = MassObject("nam", 10, Vector(1, 2, 3))
    object.set_name("123")

    assert object.name() == "123"


def test_set_mass():
    object = MassObject("nam", 10, Vector(1, 2, 3))
    object.set_mass(12)

    assert object.mass() == 12


def test_set_position():
    object = MassObject("nam", 10, Vector(1, 2, 3))
    object.set_position(Vector(4, 5))

    assert object.position().x() == 4


def test_set_speed():
    object = MassObject("nam", 10, Vector(1, 2, 3))
    object.set_speed(Vector(2, 2, 2))

    assert object.speed().x() == 2


def test_set_acceleration():
    object = MassObject("nam", 10, Vector(1, 2, 3))
    object.set_acceleration(Vector(4, 4))

    assert object.acceleration().x() == 4


def test_update_object():
    object = MassObject("nam", 10, Vector(2, 2, 2), Vector(2, 2, 2), Vector(1, 1, 1))
    object.uptade()

    assert object.position().x() == 2 + TIME*2 + 0.5*TIME**2*1
    assert object.speed().x() == 2 + TIME*1