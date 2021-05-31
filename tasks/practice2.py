from typing import List, Tuple
import re


def generate_payment_message(from_user: str, to_user: str, amount: float) -> str:
    f_u = from_user.split()
    t_u = to_user.split()
    result = f'Добрый день, {t_u[1]}!\n{f_u[1]} {list(f_u[0])[0]}. перевел вам {round(amount, 2):.2f} рублей.'
    return result


def calculate_increased_cashback(operations: List[Tuple]) -> float:
    result = 0
    for operation in operations:
        if operation[1] is True:
            result += operation[0]*0.05
        else:
            result += operation[0] * 0.01
    return result


def clean_user_login(raw_login: str) -> str:

    login = raw_login.lower().replace(' ', '').replace('"', '').replace('\'', '')
    return login

def extract_python_string(raw_string: str) -> str:

    result = ''
    r1 = raw_string.lower()
    for match in re.finditer('python', r1):
        index = match.start()

    for i in range(index, index+6):
        result += raw_string[i]

    return result

def main() -> None:
    generate_payment_message(
        'Шубин Захар Глебович', 'Вишнякова Амалия Станиславовна', 100.555
    )
    calculate_increased_cashback([(500.0, False), (100.0, True)])
    clean_user_login(' a.petrov')
    extract_python_string('Hello, Python!')


if __name__ == '__main__':
    main()
