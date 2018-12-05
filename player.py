class Player(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name
