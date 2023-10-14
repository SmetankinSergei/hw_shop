from src.classes.warehouse import Warehouse
from src.classes.item import Item


def test_add_new_item():
    warehouse = Warehouse()
    warehouse.add_new_item(Item('pencil', 5.0), 5)
    assert warehouse.all_items['pencil']['amount'] == 5
    assert warehouse.all_items['pencil']['item'].name == 'pencil'
    assert warehouse.all_items['pencil']['item'].price == 5.0


def test_add_items_by_name():
    warehouse = Warehouse()
    warehouse.add_new_item(Item('pencil', 5.0), 5)
    warehouse.add_items_by_name('pencil', 3)
    assert warehouse.all_items['pencil']['amount'] == 8


def test_del_items_by_name():
    warehouse = Warehouse()
    warehouse.add_new_item(Item('pencil', 5.0), 5)
    warehouse.del_items_by_name('pencil', 3)
    assert warehouse.all_items['pencil']['amount'] == 2


def test_get_price_all_items_by_name():
    warehouse = Warehouse()
    warehouse.add_new_item(Item('pencil', 5.0), 5)
    assert warehouse.get_price_all_items_by_name('pencil') == 25.0
