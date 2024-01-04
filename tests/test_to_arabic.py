from roman_numerals import to_arabic
import pytest

def test_base_cases():
    assert to_arabic("I") == 1
    assert to_arabic("V") == 5
    assert to_arabic("X") == 10
    assert to_arabic("L") == 50
    assert to_arabic("C") == 100
    assert to_arabic("D") == 500
    assert to_arabic("M") == 1000
   
def test_subtraction():
    assert to_arabic("MMMCDXLIV") == 3444
    assert to_arabic("LIX") == 59
    assert to_arabic("IV") == 4

def test_addition():
    assert to_arabic("III") == 3
    assert to_arabic("XX") == 20
    assert to_arabic("CCC") == 300
    assert to_arabic("MM") == 2000

def test_cleanup():
    assert to_arabic("DCCCVi I i ") == 808

def test_extra_chars():
    with pytest.raises(ValueError, match="Invalid character entered"):
        to_arabic("H")

def test_wrong_order():
    with pytest.raises(ValueError, match="Invalid input"):
        to_arabic("IL")
        to_arabic("LCXX")
        to_arabic("IXL")
        to_arabic("IXXL")

def test_wrong_notation():
    with pytest.raises(ValueError, match="Invalid input"):
        to_arabic("LL")
        to_arabic("DDD")
        to_arabic("VV")
        to_arabic("IIIIII")
        to_arabic("CCCC")
        to_arabic("XXXX")
        to_arabic("MMMMM")
        to_arabic("CCCXLIIIIII")
        to_arabic("IXIVI")

def test_max():
    assert to_arabic("MMMCMXCIX")
    with pytest.raises(ValueError, match="Maximum Roman numeral is MMMCMXCIX"):
        to_arabic("MMMM")