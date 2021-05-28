from typing import List, Tuple


def generate_payment_message(from_user: str, to_user: str,
                             amount: float) -> str:
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
    recipient_first_name = to_user.split()[1]
    sender_split = from_user.split()
    sender_short_name = sender_split[1] + " " + list(sender_split[0])[0] + "."
    result = f'Добрый день, {recipient_first_name}!\n{sender_short_name} перевел вам {amount:.2f} рублей.'

    return result


def calculate_increased_cashback(
        operations: List[Tuple[float, bool]]) -> float:
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
    result = sum(
        map(lambda pair: pair[0] * 0.05
            if pair[1] else pair[0] * 0.01, operations))

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
    login = raw_login.casefold().strip().replace("\"", "").replace("'", "")

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
    word_start_idx = raw_string.casefold().find("python")
    word_len = len("python")

    if word_start_idx != -1:
        result = raw_string[word_start_idx:word_start_idx + word_len]

    return result


def main() -> None:
    generate_payment_message('Шубин Захар Глебович',
                             'Вишнякова Амалия Станиславовна', 100.555)
    calculate_increased_cashback([(500.0, False), (100.0, True)])
    clean_user_login(' a.petrov')
    extract_python_string('Hello, Python!')


if __name__ == '__main__':
    main()
