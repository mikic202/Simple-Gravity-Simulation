from GravityPhisics import GravitiPhisics
from Object_with_mass import MassObject
from Vector import Vector
from pytest import approx


def test_init():
    assert GravitiPhisics()

def test_update_objects():
    phisics = GravitiPhisics()
    objects = [MassObject("a", 100, Vector()), MassObject("b", 100, Vector(800, 800, 800))]
    phisics.update_objects(objects)
    phisics.update_objects(objects)

    assert objects[0].position().x() == approx(0.00029477513940714197)
