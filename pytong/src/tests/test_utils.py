import pytest
from main_package.utils.utils import parse_offer, parse_offer_azair

def test_parse():
    test_offer = '23:10\nWarsaw Chopin\nWAW\n20h 20m\n1 stop\n20:30\n+1\nBen Gurion\nTLV\nFri 8 Mar\n7 nights in Tel Aviv\n11:40\nBen Gurion\nTLV\n4h 10m\nDirect\n14:50\nWarsaw Chopin\nWAW\nSelf-transfer hack\n20 kg\n2,593 zł\nSelect'
    mark = parse_offer(test_offer)
    assert len(mark) == 1
    assert mark[0] == 10

def test_regex():
    text = '+2'
    number = int(text[1:])
    assert number == 2

def test_parse_azair():
    test_offer = "THERE Thu 27/07/23 08:35 Vienna VIE 09:55 Warsaw WMI 1:20 h / no change\n\n€26.12\n "
    flight = parse_offer_azair(test_offer)
    assert flight.price == "€26.12"

test_parse_azair()