from typing import DefaultDict, List, Dict, Union
from collections import defaultdict


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

    return [i for i in numbers if i % 2 == 1]


def get_popular_category(operations: List[Dict[str, Union[str, int]]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """
    category_sums: DefaultDict[str, int] = defaultdict(int)
    for op in operations:
        category_sums[op['category']] += op['amount']

    highest_sum = 0
    highest_category = ''
    for k, v in category_sums.items():
        if v > highest_sum:
            highest_sum = v
            highest_category = k

    return highest_category


def hide_personal_info(info: Dict[str, str]) -> Dict[str, str]:
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
    sensitive_fields = ['passport_code', 'phone_number']
    strip_sensitive_info = lambda s: ''.join(
        ['*' if c.isnumeric() else c for c in s])

    info = {
        key:
        (strip_sensitive_info(field) if key in sensitive_fields else field)
        for key, field in info.items()
    }

    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
