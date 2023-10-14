from src.classes.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000)

    assert repr(item1) == 'Item: name="Смартфон", price="10000"'
    assert str(item1) == 'Смартфон'
