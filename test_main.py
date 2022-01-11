from main import *

def test_Addition():
    assert add1(3) == 4

def test_Pass():
    assert add1(1) == 2

def test_Failing():
    assert add1(2) == 4
