from main import *
import pytest

def test_Addition():
    assert add1(3) == 4

def test_Pass():
    assert add1(1) == 2
    
def test_Pass2():
    assert add1(5) == 6

def test_Failing():
    assert add1(2) == 4

@pytest.mark.skip()
def test_Skip():
    assert True
