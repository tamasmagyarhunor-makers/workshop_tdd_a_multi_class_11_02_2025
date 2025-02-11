from lib.box import Box
from lib.item import Item

def test_box_instantiates():
    # scenario
    box = Box()

    # action
    acutal = box.store
    
    #expection
    expected = []
    
    #assertion
    assert acutal == expected
    assert isinstance(box, Box)

def test_get_store_returns_store():
    box = Box()

    assert box.get_store() == []

def test_box_when_item_added_it_appears_in_the_store():
    box = Box()
    item = Item('baseball bat', 'wooden')
    box.add_item(item)

    assert box.get_store() == [item]

def test_box_collects_details_of_items():
    box = Box()
    item = Item('baseball bat', 'wooden')
    item_2 = Item('barbie', 'pink')

    box.add_item(item)
    box.add_item(item_2)

    item_descriptions = box.get_items_descriptions()

    assert item_descriptions == ['I am a baseball bat', 'I am a barbie']