from main import *
import pytest

def test_Addition():
    assert add1(13) == 14

def test_Pass():
    assert add1(11) == 12
    
def test_Pass2():
    assert add1(15) == 16

def test_Failing():
    assert add1(12) == 14
    
def test_Failing2():
    assert add1(22) == 24

@pytest.mark.skip()
def test_Skip():
    assert True
    
@pytest.mark.skip()
def test_Skip2():
    assert True
