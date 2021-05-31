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
    fromu = from_user.split()
    tou = to_user.split()
    result = F"Добрый день, {tou[1]}!\n{fromu[1]} {fromu[0][0]}. перевел вам {str('%.2f' % round(amount, 2))} рублей."
    # подготовьте данные
    # и используя функции форматирования(например, f-string) отформатируйте строку здесь
    return result


def calculate_increased_cashback(operations: List[Tuple]) -> float:
    """
    Рассчитывает размер повышенного кешбека для клиента банка.
    На все покупки - 1%
    На покупки с повышенным кешбеком - 5%

    На вход принимает:
    - operations - список кортежей - список операций в формате кортежей в которых 0-вому индексу соответствует сумма
    платежа, 1-вому индексу - является ли операция - операцией с повышенным кешбеком.
    Пример:
    [(500.0, False), (100.0, True)]

    На выходе получаем сумму кешбека на основе текущих операций.

    P.S. Чтобы пробежаться по всем операциям используйте цикл for:
    for operation in operations:
        print(operation)  # в переменной operation будет записан кортеж

    """
    result = 0
    for op in operations: result += op[0] * (0.01 + 0.04 * op[1])
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
    login = raw_login.lower().replace('"', '').replace("'", '').strip()
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
    result = raw_string[raw_string.lower().find("python") : raw_string.lower().find("python") + 6]
    return result


def main() -> None:
    print(generate_payment_message(
        'Шубин Захар Глебович', 'Вишнякова Амалия Станиславовна', 100
    ))
    calculate_increased_cashback([(500.0, False), (100.0, True)])
    clean_user_login('     ""  \' a.pe""trov   ')
    extract_python_string('Hello, PytHOn!')

if __name__ == '__main__':
    main()
