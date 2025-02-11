# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```text
As a Child
So that I can store my Items
I want to be able to store them in a Box
```

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Item:
    # User-facing properties:
    #   name: string
    #   colour: string

    def __init__(self, name, colour):
        # Parameters:
        #   name: string
        #   colour: string
        # Side effects:
        #   Sets the name and colour property of the self object
        pass # No code here yet

    def __repr__(self):
        # Parameters:
        #   None
        # Returns:
        #   Formatted details of the object
        # Side-effects
        #   None
        pass # No code here yet

    def __eq__(self):
        # Returns:
        #   Booelan (if the 2 objects properties are the same)
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

######
    item = Item('ball', 'red')

    acutal_name = item.name
    actual_colour = item.colour

    expected_name = 'ball'
    expected_colour = 'red'

    assert acutal_name == expected_name
    assert actual_colour == expected_colour


######

    item = Item('ball', 'red')

    actual = str(item)
    expected = "Item('ball', 'red')"

    assert actual == expected

######

    item_1 = Item('ball', 'red')
    item_2 = Item('ball', 'red')

    assert item_1 == item_2
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
