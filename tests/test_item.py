from lib.item import Item

def test_item_instantiates():
    # scenario
    item = Item('ball', 'red')

    # action
    acutal_name = item.name
    actual_colour = item.colour
    
    #expection
    expected_name = 'ball'
    expected_colour = 'red'
    
    #assertion
    assert acutal_name == expected_name
    assert actual_colour == expected_colour

def test_item_prints_nicely_formatted():
    item = Item('ball', 'red')

    actual = str(item)
    expected = "Item('ball', 'red') is a very nice item"

    assert actual == expected

def test_items_are_equal():
    item_1 = Item('ball', 'red')
    item_2 = Item('ball', 'red')

    assert item_1 == item_2

def test_item_get_name():
    item = Item('ball', 'red')

    assert item.get_name() == 'I am a(n) amazing ball'
