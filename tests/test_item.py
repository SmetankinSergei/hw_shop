from src.classes import Item


def test_apply_discount():
    item = Item('pencil', 5.0)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 4.0
