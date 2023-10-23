from src import DAO
from src.constants import NOT_A_NUMBER_MESSAGE


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.price = price
        Item.all.append(self)

    @property
    def name(self):
        """Геттер для названия"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Сеттер для названия"""
        new_name = new_name if len(new_name) <= 10 else new_name[:10]
        self.__name = new_name

    def __repr__(self):
        return f'{__class__.__name__}: name="{self.name}", price="{self.price}"'

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализация экземпляров через файл"""

        """Я конечно понимаю, что это делается в учебных целях, чтобы проверить,
        что мы можем пользоваться методами, переменными... Но класс, который сам создаёт экземпляры себя, при этом
        самостоятельно стучась в какой-то файл за данными, это не похоже на ООП. Смысл ООП не только в создании классов,
        но и в их взаимодействии. А тк язык позволяет нам вертеть программой как угодно, то использование ООП - это
        ответственность программиста полностью. И архитектура должна быть интуитивно и логически понятна. Для того
        ООП и используют - чтобы программа жила как в настоящем мире. Поправьте меня, если я не прав,
        но вот мой взгляд на эту программу. Есть товары. Они просто товары. Есть склад - он просто склад. Значит
        должен быть менеджер, который этим управляет. И вот ему уже можно добавлять товары,
        раскладывать их по полкам на складе и всё такое. Закомментированная строка в этом методе - то, как
        должно быть по итогу. Умолчу, что этого метода здесь вообще быть не должно, но раз есть в задании...
        В дальнейшем будет ещё один класс ShopManager, который будет заниматься выше описанным...
        В видео сказано: 'Вы сможете добавить эти проекты в портфолио...'. Но если я напишу в резюме, что владею
        навыками ООП и успешно это применяю, а потом покажу, как товар знает о количестве себе подобных на
        складе, то работу я буду искать очень долго"""
        items_data = DAO.get_all_data()
        for row in items_data:
            item = cls(row['name'], row['price'])
            Item.all.append(item)
            # shop_manager.add_new_item_to_warehouse(item, row['quantity'])

    @staticmethod
    def string_to_number(string):
        """Получение числа из строки"""
        try:
            result = float(string)
            return int(result)
        except ValueError:
            print(NOT_A_NUMBER_MESSAGE)
