def transform(number):
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Buzz'
    if number % 3 != 0  and number % 5 != 0:
        result = number
    return result


def fizzBuzz(last_number):
    for number in range(1, last_number+1):
        print(transform(number))