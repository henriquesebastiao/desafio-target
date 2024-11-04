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
