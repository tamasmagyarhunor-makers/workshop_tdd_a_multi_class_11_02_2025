class Box():
    def __init__(self):
        self.store = []
    
    def get_store(self):
        return self.store

    def add_item(self, item):
        self.store.append(item)

    def get_items_descriptions(self):
        item_descriptions = []

        for item in self.get_store():
            item_descriptions.append(item.get_name())
        
        return item_descriptions