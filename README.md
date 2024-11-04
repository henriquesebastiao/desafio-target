# Desafio técnico Target Sistemas 📝

[![CI](https://github.com/henriquesebastiao/desafio-target/actions/workflows/ci.yml/badge.svg)](https://github.com/henriquesebastiao/desafio-target/actions/workflows/ci.yml)
[![coverage](https://coverage-badge.samuelcolvin.workers.dev/henriquesebastiao/desafio-target.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/henriquesebastiao/desafio-target)

Implementação de algoritmos para questões do teste técnico para vaga de Estágio em Análise e Desenvolvimento

> [!TIP]
> Abaixo estão listadas as questões resolvidas no teste, cada questão possui um link em seu título para o arquivo com o código do algoritmo em Python, você também pode ver uma versão do código com comentários explicativos sobre a implementação clicando em `Código 💡`

## [Questão 1](one.py)

Observe o trecho de código abaixo:

```txt
int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

**R - Ao final do processamento a variável soma terá o valor de 91.**

<details><summary>Código 💡</summary><br>

```python
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1  # Soma 1 a variável k
    soma += k  # Soma o valor de k a variável soma

print(soma)  # soma = 91
```
</details>

## [Questão 2](two.py)

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

> [!IMPORTANT]
> Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.

<details><summary>Código 💡</summary><br>
    
```python
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
```
</details>

## [Questão 3](three.py)

Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

> [!IMPORTANT]
> - Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
> - Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

**Resposta:**

- O menor faturamento ocorrido no mês foi deR$ 373.78 no dia 14.
- O maior faturamento ocorrido no mês foi deR$ 48924.24 no dia 16.
- O número de dias em que o faturamento diário foi superior à média mensal foi de 10 dias.

<details><summary>Código 💡</summary><br>

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
    'O menor faturamento ocorrido no mês foi de '
    f'R$ {min_value["valor"]:.2f} no dia {min_value["dia"]}.'
)
print(
    'O maior faturamento ocorrido no mês foi de '
    f'R$ {max_value["valor"]:.2f} no dia {max_value["dia"]}.'
)
print(
    'O número de dias em que o faturamento diário '
    f'foi superior à média mensal foi de {higher_days} dias.'
)
```
</details>

## [Questão 4](four.py)

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

> [!TIP]
> Abaixo segue um gráfico com a representação percentual da análise de distribuição por estado, caso queiro ver o código em Jupyter Notebook clique [aqui](4-notebook.ipynb)

<details><summary>Código 💡</summary><br>

```python
test_data = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53,
}


def calculate_percentages(invoicing: dict[str, float]):
    total = sum(invoicing.values())
    percentages = {
        state: (value / total) * 100 for state, value in invoicing.items()
    }
    return percentages


print(
    'O percentual de representação de cada estado'
    'no faturamento mensal da distribuidora foi de:'
)

for state, percentage in calculate_percentages(test_data).items():
    print(f'{state.upper()} - {percentage:.2f}%')

```
</details>

![Gráfico](https://github.com/user-attachments/assets/90af1410-a788-4716-a347-f831de0c18fa)

## [Questão 5](5.py)

Escreva um programa que inverta os caracteres de um string.

> [!IMPORTANT]
> - Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
> - Evite usar funções prontas, como, por exemplo, reverse.

<details><summary>Código 💡</summary><br>

```python
def reverse_str(string: str):
    inverted = ''
    for i in range(len(string) - 1, -1, -1):
        inverted += string[i]
    return inverted


string = 'Test'
print('String original:', string)
print('String invertida:', reverse_str(string))
```
</details>
