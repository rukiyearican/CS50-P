import pytest

from python.week5.lesson.calculator import square

def test_positive():

    assert square(3) == 9

def test_negative():
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")