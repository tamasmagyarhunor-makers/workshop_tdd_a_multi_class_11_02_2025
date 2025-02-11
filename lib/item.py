class Item():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __repr__(self):
        return f"Item('{self.name}', '{self.colour}')"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__