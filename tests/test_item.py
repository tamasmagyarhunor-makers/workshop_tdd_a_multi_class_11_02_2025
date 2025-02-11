from lib.item import Item

def test_item_instantiates():
    item = Item('ball', 'red')

    acutal_name = item.name
    actual_colour = item.colour

    expected_name = 'ball'
    expected_colour = 'red'

    assert acutal_name == expected_name
    assert actual_colour == expected_colour

def test_item_prints_nicely_formatted():
    item = Item('ball', 'red')

    actual = str(item)
    expected = "Item('ball', 'red')"

    assert actual == expected

def test_items_are_equal():
    item_1 = Item('ball', 'red')
    item_2 = Item('ball', 'red')

    assert item_1 == item_2