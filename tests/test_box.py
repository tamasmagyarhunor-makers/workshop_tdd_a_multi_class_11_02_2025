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