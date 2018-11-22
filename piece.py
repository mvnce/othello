class Piece:
    def __init__(self, x, y, radius, owner=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.owner = owner

    def display(self):
        if self.owner == "WHITE":
            fill(255, 255, 255)
            ellipse(self.x, self.y, self.radius, self.radius)
        elif self.owner == "BLACK":
            fill(0, 0, 0)
            ellipse(self.x, self.y, self.radius, self.radius)

    def setOwner(self, owner):
        self.owner = owner

    def hasOwner(self):
        return self.owner != None

    def getOwner(self):
        return self.owner
