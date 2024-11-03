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
