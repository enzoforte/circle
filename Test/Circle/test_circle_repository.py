import pytest
import unittest
from App import app
from Src.Circle.Circle import Circle
from Src.Circle.Exception import ValueNotValidError
from App.Repository.Circle.InMemoryCircleRepository import InMemoryCircleRepository


class TestCircleRepository(object):
    
    @pytest.fixture
    def repository(self):
        repo = InMemoryCircleRepository()
        yield repo
        repo._clear()

    def testSave(self, repository):
        circle = Circle(1,1,1)
        assert isinstance(circle, Circle)
        repository.save(circle)
        stored = repository.get(circle.id)
        assert stored.getId() == circle.getId()
        assert stored.getCenter() == circle.getCenter()
        assert stored.getRadius() == circle.getRadius()
    
    def testGet(self, repository):
        circle = Circle(10,5,6)
        assert isinstance(circle, Circle)
        repository.save(circle)
        stored = repository.get(circle.id)
        assert stored.getId() == circle.getId()
        assert stored.getCenter() == circle.getCenter()
        assert stored.getRadius() == circle.getRadius()

    def testDelete(self, repository):
        circle = Circle(10,5,6)
        assert isinstance(circle, Circle)
        repository.save(circle)
        repository.delete(circle)
        stored = repository.get(circle.id)
        assert stored == None
