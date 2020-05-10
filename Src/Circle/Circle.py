from .Exception import ValueNotValidError
import uuid

class Circle : 
    _id : int
    _centerX : int
    _centerY : int
    _radius : float

    def __init__(self,  centerX = 0, centerY = 0, radius = 0):
        self.id = uuid.uuid1()
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius

    def getId(self):
        return self.id

    def getCenter(self):
        return [self.centerX, self.centerY]

    def getRadius(self):
        return self.radius

    def setCenter(self, centerX, centerY):
        self.centerX = centerX
        self.centerY = centerY

    def setRadius(self, radius):
        if(radius < 0):
            raise ValueNotValidError
        self.radius = radius

