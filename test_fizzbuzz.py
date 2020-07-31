from fizzbuzz import fizzbuzz


def test_should_return_1_given_1():
    assert 1  == fizzbuzz(1)


def test_should_return_2_given_2():
    assert 2  == fizzbuzz(2)


def test_should_return_fizz_given_3():
    assert 'Fizz' == fizzbuzz(3)


def test_should_return_buzz_given_5():
    assert 'Buzz' == fizzbuzz(5)

def test_should_return_fizz_given_6():
    assert 'Fizz' == fizzbuzz(6)