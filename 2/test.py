from two import process_line, num_same_letters, get_common_letters
from nose.tools import eq_

def test_process_line():
    eq_(process_line('abcdef'), (0, 0))
    eq_(process_line('bababc'), (1, 1))
    eq_(process_line('abbcde'), (1, 0))
    eq_(process_line('abcccd'), (0, 1))
    eq_(process_line('aabcdd'), (2, 0))
    eq_(process_line('abcdee'), (1, 0))
    eq_(process_line('ababab'), (0, 2))

def test_num_same_letters():
    eq_(num_same_letters('abcde', 'fghij'), 0)
    eq_(num_same_letters('abcde', 'axcye'), 3)
    print(get_common_letters('abcde', 'axcye'))
