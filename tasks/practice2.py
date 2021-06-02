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
    result = ''
    # подготовьте данные
    # и используя функции форматирования(например, f-string) отформатируйте строку здесь
    i = to_user.index(' ')
    i1 = to_user[i+1:len(to_user)].index(' ')
    j = from_user.index(' ')
    j1 = from_user[j+1:len(from_user)].index(' ')
    result = (
        f"Добрый день, {to_user[i+1:i+i1+1]}!\n" f"{from_user[0]}. {from_user[j+1:j+j1+1]} перевел вам {amount} рублей."
        )
    print(result)
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
    # код писать здесь
    i = 0
    for i in range(len(operations)):
        if operations[i][1] == "true":
            result = result + (operations[i][0] * 0.05)
        else:
            result = result + (operations[i][0] * 0.01)
    #print(result)
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
    import re
    login = raw_login
    i = 0
    if login.islower() == False:
        login = login.lower()
    if login[i] == ' ':
        login = login.strip()
        login = re.sub(r'\s+', ' ', login)
    login = login.replace('"', '')
    login = login.replace("'", "")
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
    import re
    res = raw_string
    i = 0
    if res.islower() == False:
        res = res.lower()
    res = res.index("python")
    result = raw_string[res:res+6]
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
