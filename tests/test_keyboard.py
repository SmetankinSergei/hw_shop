from src.classes.keyboard import Keyboard


def test_language():
    kb = Keyboard('Dark Project KD87A', 9600)
    assert str(kb.language) == 'EN'


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600)
    kb.change_lang()
    assert str(kb.language) == 'RU'
