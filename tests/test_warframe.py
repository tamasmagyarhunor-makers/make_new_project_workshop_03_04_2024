from lib.warframe import *

def test_warframe_returns_its_name():
    expected = "Mag"

    actual = warframe()

    assert expected == actual
    