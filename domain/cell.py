class Cell:

    def __init__(self):
        self.__occupied = ""

    @property
    def occupied(self):
        return self.__occupied

    @occupied.setter
    def occupied(self, value):
        self.__occupied = value

    def __str__(self):
        if self.occupied == "#":
            return "#"
        elif self.occupied == "*":
            return "*"
        else:
            return ""
