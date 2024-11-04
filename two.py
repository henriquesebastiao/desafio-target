test_number = 67


def number_in_fibonacci(number: int):
    fibonacci = [0, 1]

    while fibonacci[-1] < number:
        new_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(new_value)

    if fibonacci[-1] == number:
        print(f'O número {int(number)} pertence a sequência de Fibonacci.')
        return True

    print(f'O número {number} não pertence a sequência de Fibonacci.')
    return False


test_number = number_in_fibonacci(test_number)
