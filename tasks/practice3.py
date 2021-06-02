from typing import List, Dict, Any, Set


def filter_list(numbers: List[int]) -> List[int]:
    """
    Используя генератор списков (list comprehension) напишите код,
    который отфильтровывает все четные числа в списке.
    И возвращает результат фильтрации.

    На вход:
    - numbers - список состоящий из чисел

    На выходе:
    список только из нечетных чисел
    """

    return [num for num in numbers if num % 2 == 1]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    categories: Set = set()
    sum = {}               # Будет иметь структуру {'название категории': 100}, причём без повторений категорий
    for operation in operations:
        if operation['category'] in categories:
            sum[operation['category']] += operation['amount']
        else:
            sum[operation['category']] = operation['amount']
            categories.add(operation['category'])
    max_amount = 0
    max_category = ''
    for key in sum.keys():
        if sum[key] > max_amount:
            max_amount = sum[key]
            max_category = key
    return max_category


def hide_personal_info(info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Функция принимает на вход словарь содержащий информацию о клиенте.
    В словаре могут быть персональные данные клиента: ключи passport_code и phone_number.
    Если поля присутствуют - нужно защитить эти данные от злоумышленников.
    Для этого заменим все цифры в значениях этих полей на символ *.

    На вход:
    - info - словарь содержащий персональные данные клиента

    На выходе:
    - словарь в котором все персональные данные из описания функции - скрыты по алгоритму выше.
    """

    try:
        temp = str(info['passport_code'])
        code_passport = ['*' if symbol != ' ' else symbol for symbol in temp]
        info['passport_code'] = ''.join(code_passport)
    except KeyError:
        pass
    try:
        temp = str(info['phone_number'])
        code_num = ['*' if symbol != '+' else symbol for symbol in temp]
        info['phone_number'] = ''.join(code_num)
    except KeyError:
        pass
    # впишите ваш код здесь
    return info


def main() -> None:
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
    get_popular_category(OPERATIONS)


if __name__ == '__main__':
    main()
