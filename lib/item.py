class Item():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __repr__(self):
        return f"Item('{self.name}', '{self.colour}') is a very nice item"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_name(self):
        return f"I am a(n) amazing {self.name}"