class Piece:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def display(self):
        fill(0, 0, 0)
        ellipse(self.x, self.y, self.radius, self.radius)
