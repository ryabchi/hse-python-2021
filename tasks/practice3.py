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

    return [x for x in numbers if x % 2]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.
    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]
    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    c = {i:0 for i in [j['category'] for j in operations]}
    for i in operations:
        c[i['category']] += i['amount']
    return max(c, key=lambda x: c[x])


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

    for x in info:
        if x == 'passport_code' or x == 'phone_number':
            info[x] =''.join(['*' if s.isdecimal() else s for s in info[x]])
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()