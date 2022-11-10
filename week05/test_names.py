from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Cena") == "Cena; John"
    assert make_full_name("Guadalupe", "Sanchez-Gonzalez") == "Sanchez-Gonzalez; Guadalupe"


def  test_extract_family_name():
    assert extract_family_name("Gates; Bill") == "Gates"
    assert extract_family_name("William; Jones") == "William"


def test_extract_given_name():
    assert extract_given_name("Thomases; Sabrina") == "Sabrina"
    assert extract_given_name("Anderson; Reed") == "Reed"

pytest.main(["-v", "--tb=line", "-rN", __file__])