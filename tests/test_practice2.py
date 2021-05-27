import pytest

from tasks.practice2 import (
    generate_payment_message,
    calculate_increased_cashback,
    clean_user_login,
    extract_python_string,
)


@pytest.mark.parametrize(
    ('from_user', 'to_user', 'amount', 'expected'),
    [
        (
            'Галкин Николай Петрович',
            'Сидоров Григорий Мирославович',
            100.5555,
            'Добрый день, Григорий!\nНиколай Г. перевел вам 100.56 рублей.',
        ),
        (
            'Иванов Александр Петрович',
            'Петров Евгений Сергеевич',
            100,
            'Добрый день, Евгений!\nАлександр И. перевел вам 100.00 рублей.',
        ),
    ],
    ids=['High accuracy', 'Integer'],
)
def test_generate_payment_message(from_user, to_user, amount, expected):
    assert generate_payment_message(from_user, to_user, amount) == expected


@pytest.mark.parametrize(
    ('operations', 'cashback'),
    [
        ([(500, True), (200, False), (700, True), (100, False)], 63),
        (
            [
                (500, False),
                (200, False),
            ],
            7,
        ),
        (
            [
                (500, True),
                (200, True),
            ],
            35,
        ),
        ((), 0),
    ],
)
def test_calculate_increased_cashback(operations, cashback):
    assert calculate_increased_cashback(operations) == cashback


@pytest.mark.parametrize(
    ('raw_login', 'login'),
    [
        ('  e.petrov  ', 'e.petrov'),
        ('e.PETROV', 'e.petrov'),
        ('e.pe"tro\'v  ', 'e.petrov'),
    ],
)
def test_clean_user_login(raw_login, login):
    assert clean_user_login(raw_login) == login


@pytest.mark.parametrize(
    ('raw_string', 'extracted'),
    [
        ('Hello! This is python language!', 'python'),
        ('Python the best language!', 'Python'),
        ('How use pYtHon fo data analyzing?', 'pYtHon'),
        ('pythoN', 'pythoN'),
    ],
)
def test_extract_python_string(raw_string, extracted):
    assert extract_python_string(raw_string) == extracted
