from typing import List, Tuple

def generate_payment_message(from_user: str, to_user: str, amount: float) -> str:

    return 'Добрый день, ' + to_user.split(' ')[1] + '!\n' + from_user.split(' ')[1] + ' ' + from_user.split(' ')[0][0] + \
        '. ' + ['перевела' if (from_user.split(' ')[2][-1] == 'а') else 'перевел'][0] + ' вам ' + str(round(amount, 2)) + ' рублей.'


def calculate_increased_cashback(operations: List[Tuple]) -> float:

    return sum(list(map(lambda x: x[0] * 0.05 if x[1] else x[0] * 0.01, operations)))


def clean_user_login(raw_login: str) -> str:

    return ''.join([i.lower() for i in raw_login if (i not in ['\'', '\"', ' '])])


def extract_python_string(raw_string: str) -> str:

    return raw_string[raw_string.lower().find('python'):raw_string.lower().find('python') + 6]


def main() -> None:
    calculate_increased_cashback([(500.0, False), (100.0, True)])
    clean_user_login(' a.petrov')
    extract_python_string('Hello, PyThoN!')


if __name__ == '__main__':
    main()
