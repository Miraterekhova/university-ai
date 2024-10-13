import math
import pytest

def filter_is_positive(x):
    if x is None:
        return False
    return x > 0

def map_concatenate_strings(str1, str2):
    return str1 + str2

def test_filter():
    assert list(filter(filter_is_positive, [1, 2, 3, 4, 5, 6, 7, 8, 9]))==[1,2,3,4,5,6,7,8,9]
    assert list(filter(filter_is_positive,[-1, 2, -3, 4, 5, 6, 7, 8, 9]))==[2, 4, 5, 6, 7, 8, 9], 'negative number'
    assert list(filter(filter_is_positive,[]))==[], 'empty list'
    assert list(filter(filter_is_positive,[0, 1, 2]))==[1, 2], 'ziro recognized'
    assert list(filter(filter_is_positive,[None, 1, 2]))==[1, 2], 'None recognized'


def test_map():
    assert list(map(map_concatenate_strings,['bannana'], ['apple']))==['bannanaapple']
    assert list(map(map_concatenate_strings,'1', '2'))==['12']
    assert list(map(map_concatenate_strings,[1], [2]))==[3]
    assert len(list(map(map_concatenate_strings,['1'], ['2'])))==1
    assert len(list(map(map_concatenate_strings,['1'], ['2']))[0])==2



def test_sorted():
    assert sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])==[1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert len(sorted([3, 1, 4, 1, 5, 9, 2, 6, 5]))==9
    assert sorted(['apple', 'banana', 'cherry', 'date', 'elderberry'])==['apple', 'banana', 'cherry', 'date', 'elderberry']
    assert sorted( [3, 1, 4, 1, 5, 9, 2, 6, 5], reverse=True) == [9, 6, 5, 5, 4, 3, 2, 1, 1]
    assert sorted([
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20},
    ], key=lambda x: x['name']) == [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20},
    ]
    assert sorted([]) == []



def test_pi():
    assert math.pi > 3.14
    assert math.pi < 3.15
    assert abs(math.pi - 3.14159) < 1e-5


def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(16) == 4
    assert math.sqrt(0) == 0
    with pytest.raises(ValueError):
        math.sqrt(-1)
def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(5, 0) == 1
    assert math.pow(2, -2) == 0.25
    assert math.pow(0, 5) == 0
    with pytest.raises(TypeError):
        math.pow(2)
    with pytest.raises(TypeError):
        math.pow(2, 3, 4)

def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(0, 0) == 0
    assert math.hypot(1, 1) == math.sqrt(2)
    assert math.hypot(1, 2, 3)==math.sqrt(1**2 + 2**2 + 3**2)
    with pytest.raises(TypeError):
        math.hypot(1)















