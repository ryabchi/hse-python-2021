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

    max_cat = ''
    max_am = 0
    for operation in operations:
        if operation['amount'] > max_am:
            max_am = operation['amount']
            max_cat = operation['category']
        return max_cat


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

    newstr = ''
    if 'passport_code' in info.keys():
        for i in info['passport_code']:
            if i.isdigit():
                newstr += '*'
            else:
                newstr += i
        info['passport_code'] = newstr
        newstr = ''

    if 'phone_number' in info.keys():
        for i in info['phone_number']:
            if i.isdigit():
                newstr += '*'
            else:
                newstr += i
        info['phone_number'] = newstr
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
