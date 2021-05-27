from typing import List, Tuple


def generate_payment_message(from_user: str, to_user: str, amount: float) -> str:
    """
    Генерирует сообщение о переводе денежных средств.

    На вход принимает:
    - from_user - строка - ФИО клиента от которого пришел перевод (например, Иванов Александр Петрович)
    - to_user - строка - ФИО клиента кому пришел перевод (например, Петров Евгений Сергеевич)
    - amount - число с плавающей запятой - сумма перевода

    На выходе получаем строку с текстом, смотрите пример ниже:
    Добрый день, Евгений!
    Александр И. перевел вам 100.56 рублей.
    """
    name: str = to_user.split(' ')[1]
    from_user_initial: List[str] = from_user.split(' ')   
    result = f'Добрый день, {name}!\n{from_user_initial[1]} {from_user_initial[0][0]}. перевел вам {amount:.2f} рублей.'
    # подготовьте данные
    # и используя функции форматирования(например, f-string) отформатируйте строку здесь
    return result


def calculate_increased_cashback(operations: List[Tuple]) -> float:
    result: float = 0
    cashback: dict[bool, lambda:float] = { True: lambda a: a * 0.05, False: lambda a: a * 0.01 }
    for item in operations:
        result += cashback[item[1]](item[0])
    # код писать здесь
    return result


def clean_user_login(raw_login: str) -> str:
    login = raw_login.lower().strip().replace('\'', '').replace('"', '')
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

    # код писать здесь
    return login


def extract_python_string(raw_string: str) -> str:
    string: str = raw_string.lower()
    start_index: int = string.index('python')
    result = ''
    result = raw_string[start_index:start_index + 6]
    """
    Функция извлекает слово "python" из строки с сохранением оригинального написания.

    На вход принимает:
    - raw_string - строка - строка содержащая слово python буквами разного регистра - например "Hello, PythoN!"

    На выходе:
    Извлекаем слово python в том виде, как оно прописано в исходной строке.
    Например, к строке выше вернем: "PythoN"
    """
    # код писать здесь
    return result


def main() -> None:
    print(generate_payment_message(
        'Шубин Захар Глебович', 'Вишнякова Амалия Станиславовна', 100.555
    ))
    print(calculate_increased_cashback([(500.0, False), (100.0, True)]))
    print(clean_user_login(' a.petrov'))
    extract_python_string('Hello, Python!')


if __name__ == '__main__':
    main()
