from typing import List, Dict, Any

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

    # впишите ваш код здесь
    return [x for x in numbers if (x % 2) != 0]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    # впишите ваш код здесь
    max_category = ''
    max_amount = -1
    bufdict = {}
    for operation in operations:
        if operation['category'] in bufdict.keys():
            bufdict[operation['category']] += operation['amount']
        else:
            bufdict[operation['category']] = operation['amount']

    print(bufdict)
    for operation in bufdict.items():
        if operation[1] > max_amount:
            max_amount = operation[1]
            max_category = operation[0]
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

    # впишите ваш код здесь
    newstr = ''
    if 'passport_code' in info.keys():
        for symbol in info['passport_code']:
            if symbol.isdigit():
                newstr += '*'
            else:
                newstr += symbol
        info['passport_code'] = newstr
        newstr = ''

    if 'phone_number' in info.keys():
        for symbol in info['phone_number']:
            if symbol.isdigit():
                newstr += '*'
            else:
                newstr += symbol
        info['phone_number'] = newstr
    return info


def main() -> None:
    pass
    print(filter_list([1, 2, 3, 4, 5, 6, 7]))
    d = {'passport_code': '12312432432', 'phone_number': '12355324757'}
    print(hide_personal_info(d))
if __name__ == '__main__':
    main()
