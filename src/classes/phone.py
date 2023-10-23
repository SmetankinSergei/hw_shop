from src.classes.item import Item


class Phone(Item):
    def __init__(self, name, price, sim_amount):
        super().__init__(name, price)
        if sim_amount == 0:
            sim_amount = 1
        self.__sim_amount = sim_amount

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.sim_amount})"

    @property
    def sim_amount(self):
        return self.__sim_amount
