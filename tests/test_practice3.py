import pytest

from tasks.practice3 import filter_list, get_popular_category, hide_personal_info


@pytest.mark.parametrize(
    ('numbers', 'result'), [
        ([], []),
        ([2], []),
        ([1, 2, 3, 4, 5], [1, 3, 5]),
        ([1, 3, 5], [1, 3, 5])
    ]
)
def test_filter_list(numbers, result):
    assert filter_list(numbers) == result


OPERATIONS = [
    {'category': 'супермаркеты', 'amount': 3680}, {'category': 'рестораны', 'amount': 4649},
    {'category': 'супермаркеты', 'amount': 1388}, {'category': 'рестораны', 'amount': 1566},
    {'category': 'дом, ремонт', 'amount': 646}, {'category': 'дом, ремонт', 'amount': 4524},
    {'category': 'дом, ремонт', 'amount': 2751}, {'category': 'супермаркеты', 'amount': 1411},
    {'category': 'рестораны', 'amount': 2140}, {'category': 'рестораны', 'amount': 3672},
    {'category': 'рестораны', 'amount': 31}, {'category': 'дом, ремонт', 'amount': 1592},
    {'category': 'рестораны', 'amount': 1514}, {'category': 'транспорт', 'amount': 457},
    {'category': 'транспорт', 'amount': 577}, {'category': 'дом, ремонт', 'amount': 1799},
    {'category': 'транспорт', 'amount': 3271}
]


@pytest.mark.parametrize(
    ('operations', 'result'), [
        (OPERATIONS, 'рестораны'),
        ([{'category': 'супермаркеты', 'amount': 3680}], 'супермаркеты')
    ]
)
def test_get_popular_category(operations, result):
    assert get_popular_category(operations) == result


@pytest.mark.parametrize(
    ('info', 'result'), [
        (
                {'name': 'Jhon', 'lastname': 'Doe', 'passport_code': '2200 775511', 'phone_number': '+78005553535'},
                {'name': 'Jhon', 'lastname': 'Doe', 'passport_code': '**** ******', 'phone_number': '+***********'},
        ),
        (
                {'name': 'Jhon', 'lastname': 'Doe', 'passport_code': '2200 775511'},
                {'name': 'Jhon', 'lastname': 'Doe', 'passport_code': '**** ******'},
        ),
        (
                {'name': 'Jhon', 'lastname': 'Doe', 'phone_number': '+78005553535'},
                {'name': 'Jhon', 'lastname': 'Doe', 'phone_number': '+***********'},
        )
    ]
)
def test_hide_personal_info(info, result):
    assert hide_personal_info(info) == result
