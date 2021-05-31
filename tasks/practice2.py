from typing import List, Tuple


def generate_payment_message(from_user: str, to_user: str, amount: float) -> str:
    result = ''
    spl_to = to_user.split()
    spl_from = from_user.split()
    result = f"Доборый день, {spl_to[1]}!\n{spl_from[1]} {spl_from[0][0]}. перевел вам {amount:.2f} рублей."
    return result


def calculate_increased_cashback(operations: List[Tuple]) -> float:
    result = 0
    for operation in operations:
        if operation[1]:
            cash = operation[0]*0.05
        else:
            cash = operation[0] * 0.01
        result += cash
    return result


def clean_user_login(raw_login: str) -> str:
    login = ''
    for symb in raw_login:
        if not(symb == ' ' or symb == '\'' or symb == '"'):
            login += symb.lower()
    return login


def extract_python_string(raw_string: str) -> str:
    result = ''
    tmp = raw_string.lower().find('python')
    result = raw_string[tmp: tmp + 6]
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