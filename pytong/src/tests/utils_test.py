import pytest
from main_package.utils.utils import parse_offer

def test_parse():
    test_offer = '23:10\nWarsaw Chopin\nWAW\n20h 20m\n1 stop\n20:30\n+1\nBen Gurion\nTLV\nFri 8 Mar\n7 nights in Tel Aviv\n11:40\nBen Gurion\nTLV\n4h 10m\nDirect\n14:50\nWarsaw Chopin\nWAW\nSelf-transfer hack\n20 kg\n2,593 zł\nSelect'
    mark = parse_offer(test_offer)
    assert len(mark) == 1
    assert mark[0] == 10

def test_regex():
    text = '+2'
    number = int(text[1:])
    assert number == 2