import five
import four
import one
import three
import two


def test_soma():
    assert one.soma == 91


def test_fibonacci():
    assert two.number_in_fibonacci(34)


def test_number_test_fibonacci():
    assert not two.test_number


def test_number_test_fibonacci_valid_number():
    assert two.number_in_fibonacci(34)


def test_lowest_billing_value():
    assert three.min_value['valor'] == 373.7838
    assert three.min_value['dia'] == 14
    assert three.max_value['valor'] == 48924.2448
    assert three.max_value['dia'] == 16
    assert three.higher_days == 10


def test_calculate_percentages():
    test_data = {
        'sp': 67836.43,
        'rj': 36678.66,
        'mg': 29229.88,
        'es': 27165.48,
        'outros': 19849.53,
    }

    percentages = four.calculate_percentages(test_data)

    expected_percentages = {
        'sp': 37.53,
        'rj': 20.29,
        'mg': 16.17,
        'es': 15.03,
        'outros': 10.98,
    }

    for state, expected_value in expected_percentages.items():
        assert round(percentages[state], 2) == expected_value


def test_reverse_string():
    assert five.reverse_str('test') == 'tset'
