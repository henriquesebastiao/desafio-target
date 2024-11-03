# Desafio técnico Target Sistemas 📝

## Questão 1

Observe o trecho de código abaixo:

```txt
int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

```python
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)  # soma = 91
```

**R - Ao final do processamento a variável soma terá o valor de 91.**

## Questão 2

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.

```python
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
```

## Questão 3

Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

**IMPORTANTE:**

- Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
- Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

```python
import json

with open('dados.json', encoding='utf-8') as file:
    data = json.load(file)

biling_days = 0
min_value = data[0]
max_value = data[0]
monthly_amount = 0

for day in data:
    if day['valor'] > 0:
        biling_days += 1

    if day['valor'] < min_value['valor'] and day['valor'] != 0:
        min_value = day

    if day['valor'] > max_value['valor']:
        max_value = day

    monthly_amount += day['valor']

average = monthly_amount / biling_days

higher_days = 0
for day in data:
    if day['valor'] > average:
        higher_days += 1

print(
    'O menor faturamento ocorrido no mês foi de'
    f'R$ {min_value["valor"]:.2f} no dia {min_value["dia"]}.'
)
print(
    'O maior faturamento ocorrido no mês foi de'
    f'R$ {max_value["valor"]:.2f} no dia {max_value["dia"]}.'
)
print(
    'O número de dias em que o faturamento diário'
    f'foi superior à média mensal foi de {higher_days} dias.'
)
```

## Questão 4

Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

**Resposta:**

- SP - 37.53%
- RJ - 20.29%
- MG - 16.17%
- ES - 15.03%
- OUTROS - 10.98%

```python
invoicing = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53,
}

total = sum(invoicing.values())

print(
    'O percentual de representação de cada estado'
    'no faturamento mensal da distribuidora foi de:'
)

for state, value in invoicing.items():
    print(f'{state.upper()} - {((value / total) * 100):.2f}%')
```

## Questão 5

Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

- Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

- Evite usar funções prontas, como, por exemplo, reverse.

```python
string = input('Insira a string para ser invertida: ')
inverted = ''

for i in range(len(string) - 1, -1, -1):
    inverted += string[i]

print('String original:', string)
print('String invertida:', inverted)

```
