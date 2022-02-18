import pytest

@pytest.fixture
def input_str():
    input = 'ABC'
    return input

def test_uppercase(input_str):
    assert input_str.isupper()


def test_lowercase(input_str):
    try:
        assert input_str.isupper()
    except AssertionError:
        pass

@pytest.mark.parametrize("input, output",[('abc','ABC'),('asd','ASD'),('fff','fff'),('asdd','asdd')])
def test_str_eq(input, output):
    try:
        assert input.upper() == output
    except AssertionError:
        assert input == output