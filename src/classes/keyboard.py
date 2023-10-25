from src import languages
from src.classes.item import Item


class Keyboard(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.__language = languages.Language.EN

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == languages.Language.EN:
            self.__language = languages.Language.RU
        else:
            self.__language = languages.Language.EN
