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
