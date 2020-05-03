import abc
from .Circle import Circle

class CircleRepository(abc.ABC):
 
    @abc.abstractmethod
    def add(self, batch: Circle):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Circle:
        raise NotImplementedError
    
    @abc.abstractmethod
    def edit(self, circle: Circle):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, circle: Circle):
        raise NotImplementedError

