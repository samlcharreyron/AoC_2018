from five import react_once, reacts, react, rotate
from nose.tools import eq_

def test_react_once():
    string = 'abBA'
    eq_(react_once(string), 'aA')
    string = 'aabAAB'
    eq_(react_once(string), string)

def test_rotate():
    string = 'rotate'
    eq_(rotate(rotate(string), -1), string)

def test_react():
    string = 'aabAAB'
    eq_(react(string), string)

    string = 'abBA'
    eq_(react(string), '')

    string = 'dabAcCaCBAcCcaDA'
    eq_(react(string), 'dabCBAcaDA')

def test_reacts():
    assert(not(reacts('aa')))
    assert(not(reacts('AA')))
    assert(not(reacts('aB')))
    assert(reacts('aA'))


