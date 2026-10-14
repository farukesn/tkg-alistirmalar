import pytest
from alistirma import isaret, donem_notu, harf_say, faktoriyel, gecenler

def test_isaret():
    assert isaret(5) == "pozitif"
    assert isaret(-3) == "negatif"
    assert isaret(0) == "sıfır"

def test_donem_notu():
    assert donem_notu(50, 70) == 62.0
    assert donem_notu(100, 100) == 100.0
    assert donem_notu(0, 0) == 0.0

def test_harf_say():
    assert harf_say("merhaba", "a") == 2
    assert harf_say("Ankara", "a") == 2
    assert harf_say("Ankara", "A") == 1
    assert harf_say("python", "z") == 0

def test_faktoriyel():
    assert faktoriyel(0) == 1
    assert faktoriyel(1) == 1
    assert faktoriyel(5) == 120
    assert faktoriyel(4) == 24

def test_gecenler():
    assert gecenler([70, 45, 90]) == [70, 90]
    assert gecenler([50, 59, 30]) == []
    assert gecenler([60, 100, 80]) == [60, 100, 80]
