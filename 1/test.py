from one import decode, decode2
from nose.tools import eq_

def test_decode_1():
    current = decode('1\n1\n1\n')
    eq_(current, 3)

def test_decode_2():
    current = decode('1\n1\n-2\n')
    eq_(current, 0)

def test_decode2_1():
    freq = decode2('1\n-1\n')
    eq_(freq, 0)

def test_decode2_2():
    freq = decode2('3\n3\n4\n-2\n-4\n')
    eq_(freq, 10) 

def test_decode2_3():
    #-6, +3, +8, +5, -6 
    freq = decode2('-6\n3\n8\n5\n-6\n')
    eq_(freq, 5)
