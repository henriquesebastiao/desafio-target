while True:
    number = input('Informe um número: ')
    if not number.isdigit:
        print('Você não informou um número, tente novamente.\n')
        continue
    number = float(number)
    break

fibonacci = [0, 1]

while fibonacci[-1] < number:
    new_value = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_value)

if fibonacci[-1] == number:
    print(f'O número {int(number)} pertence a sequência de Fibonacci.')
else:
    print(f'O número {number} não pertence a sequência de Fibonacci.')
