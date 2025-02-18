from lib.box import Box
from unittest.mock import Mock

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
    item = Mock()
    box.add_item(item)

    assert box.get_store() == [item]

def test_box_collects_details_of_items():
    box = Box()
    mock = Mock()
    mock_2 = Mock()
    mock.get_name.return_value = "I am a(n) amazing baseball bat"
    mock_2.get_name.return_value = "I am a(n) amazing barbie"

    box.add_item(mock)
    box.add_item(mock_2)

    item_descriptions = box.get_items_descriptions()

    assert item_descriptions == ['I am a(n) amazing baseball bat', 'I am a(n) amazing barbie']