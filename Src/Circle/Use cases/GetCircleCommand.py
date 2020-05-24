
class GetCircleCommand:

    _id : int

    def __init__ (self, id : int):
        self.id = id

    def getId (self) -> int:
        return self.id