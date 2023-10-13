from src.DAO import get_all_data


def test_get_all_data():
    assert type(get_all_data()) == list
    for item in get_all_data():
        assert type(item) == dict
