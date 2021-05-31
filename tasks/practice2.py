from typing import List, Tuple


def generate_payment_message(from_user: str, to_user: str, amount: float) -> str:
    result = ''
    spl_to = to_user.split()
    spl_from = from_user.split()
    result = f"Доборый день, {spl_to[1]}!\n {spl_from[1]} {spl_from[0][0]}. перевел вам {amount:.2f} рублей."
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
    """
    Приводит логин пользователя к виду, который используется в нашей системе.
    Требования к логину:
    - буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    На вход принимает:
    - raw_login - строка - логин в том виде, как его ввел пользователь
    На выходе:
    Строка с очищенным логином.
    """
    login = None
    # код писать здесь
    return login


def extract_python_string(raw_string: str) -> str:
    """
    Функция извлекает слово "python" из строки с сохранением оригинального написания.
    На вход принимает:
    - raw_string - строка - строка содержащая слово python буквами разного регистра - например "Hello, PythoN!"
    На выходе:
    Извлекаем слово python в том виде, как оно прописано в исходной строке.
    Например, к строке выше вернем: "PythoN"
    """
    result = ''
    # код писать здесь
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