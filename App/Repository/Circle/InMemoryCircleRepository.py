from Src.Circle.CircleRepository import CircleRepository
from Src.Circle import Circle


class InMemoryCircleRepository(CircleRepository):

    def __init__(self):
        self.circles = {}
        
    def save(self, circle:Circle):
        id = circle.getId()
        self.circles[id] = circle

    def get(self, id) -> Circle:
       return self.circles.get(id)

    def delete(self, circle: Circle):
       del self.circles[circle.getId()]

    def _clear(self):
        self.circles = {}