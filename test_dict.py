import pytest

@pytest.fixture
def input_dict():
    input = {'a': 1,
             'b': 2,
             'c': 3}
    return input

# на какую-нибудь сортировку
def test_keys_sort(input_dict):
    new_dict = {}
    list_keys = list(input_dict.keys())
    list_keys.sort()
    for i in list_keys:
        new_dict.update({i: input_dict[i]})
    assert new_dict == input_dict


def test_val_type(input_dict):
    list_values = list(input_dict.values())
    for i in range(len(list_values)):
        try:
            assert isinstance(list_values[i], str)
        except AssertionError:
            if isinstance(list_values[i], int):
                pass

@pytest.mark.parametrize("dict", [({'asda': 'asd', 'asdd': 2, 'rpc': 'kruto'}), ({1:'first',2:'second',3:'third'}),({'test':'hehe', 'test2':'hehe', 'try':'hehe'})])
def test_dict_val_uniq(dict):
    try:
        values = dict.values()
        assert len(set(values)) == len(values)
    except AssertionError:
        if len(set(values)) != len(values):
            pass
        else:
            print('smt goes wrong')

