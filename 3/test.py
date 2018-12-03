from nose.tools import eq_
from three import process_code, get_cids

def test_process_code():
    cid, y, x, cols, rows = process_code('#222 @ 1,3: 4x4')
    eq_(cid, 222)
    eq_(y, 1)
    eq_(x, 3)
    eq_(cols, 4)
    eq_(rows, 4)

def test_get_cids():
    with open('test.txt') as f:
        lines = f.read().splitlines()
        print get_cids(lines)
