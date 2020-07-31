from fizzbuzz import transform, fizzBuzz


def test_should_return_1_given_1():
    assert 1  == transform(1)


def test_should_return_2_given_2():
    assert 2  == transform(2)


def test_should_return_fizz_given_3():
    assert 'Fizz' == transform(3)


def test_should_return_buzz_given_5():
    assert 'Buzz' == transform(5)


def test_should_return_fizz_given_6():
    assert 'Fizz' == transform(6)


def test_should_return_buzz_given_10():
    assert 'Buzz' == transform(10)


def test_should_return_fizzbuzz_given_15():
    assert 'FizzBuzz' == transform(15)


def test_should_return_fizzbuzz_given_30():
    assert 'FizzBuzz' == transform(30)


def test_fizzbuzz_should_print_number_till_15(capsys):
    fizzBuzz(15)
    captured = capsys.readouterr()
    expected_output = '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n'

    assert captured.out == expected_output

