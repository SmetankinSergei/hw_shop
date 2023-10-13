import csv

from src.constants import ITEMS_CVS_PATH


def get_all_data():
    """Получение всех данных из файла"""
    with open(ITEMS_CVS_PATH) as file:
        items_data = []
        reader = csv.DictReader(file)
        for row in reader:
            items_data.append(row)
        return items_data
