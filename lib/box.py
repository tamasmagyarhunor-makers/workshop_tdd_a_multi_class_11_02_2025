class Box():
    def __init__(self):
        self.store = []
    
    def get_store(self):
        return self.store

    def add_item(self, item):
        self.store.append(item)