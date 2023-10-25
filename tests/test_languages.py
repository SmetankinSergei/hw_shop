import pytest

from src import languages


def test_str():
    lang = languages.Language.EN
    assert str(lang) == 'EN'
    with pytest.raises(AttributeError):
        lang = languages.Language.CH
        assert str(lang) == 'CH'
