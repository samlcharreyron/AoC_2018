from five import react_once, reacts, react
from nose.tools import eq_

def test_react_once():
    string = 'abBA'
    eq_(react_once(string), 'aA')
    string = 'aabAAB'
    eq_(react_once(string), string)

def test_react():
    string = 'aabAAB'
    eq_(react(string), len(string))

    string = 'abBA'
    eq_(react(string), 0)

    string = 'dabAcCaCBAcCcaDA'
    eq_(react(string), len('dabCBAcaDA'))

def test_reacts():
    assert(not(reacts('aa')))
    assert(not(reacts('AA')))
    assert(not(reacts('aB')))
    assert(reacts('aA'))


