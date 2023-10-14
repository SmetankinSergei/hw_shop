from src.classes.item import Item


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    print(len(Item.all))
    assert len(Item.all) == 10


def test_apply_discount():
    item = Item('pencil', 5.0)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 4.0


def test_name():
    item = Item('pencil', 5.0)
    assert item.name == 'pencil'
    item.name = 'pencil_red'
    assert item.name == 'pencil_red'
    item.name = 'pencil_black'
    assert item.name == 'pencil_bla'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000)
    assert repr(item1) == 'Item: name="Смартфон", price="10000"'


def test_str():
    item1 = Item("Смартфон", 10000)
    assert str(item1) == 'Смартфон'
