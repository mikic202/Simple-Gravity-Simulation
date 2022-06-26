from Object_with_mass import MassObject
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