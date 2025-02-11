from lib.box import Box
from lib.item import Item

def test_integration_box_collects_details_of_items():
    box = Box()
    item = Item('baseball bat', 'wooden')
    item_2 = Item('barbie', 'pink')

    box.add_item(item)
    box.add_item(item_2)

    item_descriptions = box.get_items_descriptions()

    assert item_descriptions == ['I am a(n) amazing baseball bat', 'I am a(n) amazing barbie']