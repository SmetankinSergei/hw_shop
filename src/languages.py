from enum import Enum


class Language(Enum):
    EN = 0
    RU = 1

    def __str__(self):
        return self.name
