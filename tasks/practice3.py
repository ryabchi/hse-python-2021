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

    rlist =  [x for x in numbers if x % 2]
    return rlist


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    count = dict()
    retst = ""
    maxc = 0
    for d in operations:
        if d['category'] in count.keys():
            count[d['category']] += d['amount']
        else:
            count[d['category']] += 0
            if count[d['category']] > maxc:
                retst = d['category']
                maxc =  count[d['category']] 
    return retst


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

    if 'passport_code' in info.keys():
        for x in info['passport_code']:
            if x.isdigit():
                x = '*'
    if 'phone_number' in info.keys():
        for x in info['phone_number']:
            if x.isdigit():
                x = '*'
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
