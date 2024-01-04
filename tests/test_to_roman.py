from roman_numerals import to_roman
import pytest

def test_base_cases():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"

def test_addition():
    assert to_roman(3) == "III"
    assert to_roman(300) == "CCC"
    assert to_roman(2000) == "MM"

def test_fours():
    assert to_roman(4) == "IV"
    assert to_roman(40) == "XL"
    assert to_roman(400) == "CD"

def test_nines():
    assert to_roman(9) == "IX"
    assert to_roman(90) == "XC"
    assert to_roman(900) == "CM"

def test_greedy():
    assert to_roman(8) == "VIII"
    assert to_roman(7) == "VII"
    assert to_roman(6) == "VI"
    assert to_roman(80) == "LXXX"
    assert to_roman(70) == "LXX"
    assert to_roman(60) == "LX"
    assert to_roman(800) == "DCCC"
    assert to_roman(700) == "DCC"
    assert to_roman(600) == "DC"

def test_complex():
    assert to_roman(473) == "CDLXXIII"
    assert to_roman(66) == "LXVI"
    assert to_roman(2989) == "MMCMLXXXIX"

def test_max():
    assert to_roman(3999) == "MMMCMXCIX"
    with pytest.raises(ValueError, match="Maximum number that can be represented is 3999"):
        to_roman(4000)