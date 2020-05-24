import unittest
from App import app
from Src.Circle.Circle import Circle
from Src.Circle.Exception import ValueNotValidError
import uuid

class TestCircle(unittest.TestCase):
 
    def testCreatCircle(self):
        circle : Circle = Circle(0, 0, 11)
        assert circle.getCenter() == [0,0]
        assert circle.getRadius() == 11

    def testUpdateCircle (self):
        circle : Circle = Circle(1, 5, 11)
        assert circle.getCenter() == [1,5]
        assert circle.getRadius() == 11
        circle.setCenter(9,9)
        circle.setRadius(3)
        assert circle.getCenter() == [9,9]
        assert circle.getRadius() == 3
    
    def testRadiusNegativeError(self):
        circle : Circle = Circle()
        try:
            circle.setRadius(-10)
            assert False
        except ValueNotValidError:
            assert True

    def testTwoCirclesAreNotEqual (self):
        circleA : Circle = Circle(1, 0, 0)
        circleB : Circle = Circle(1, 0, 0)
        assert circleA != circleB
    
    def testCirclIdIsUUID (self):
        circle : Circle = Circle(1, 0, 0)
        try:
            uuid.UUID(str(circle.id))
            assert True
        except ValueError:
            assert False

    