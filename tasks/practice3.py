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
    return [x for x in numbers if x % 2 == 1]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """
    unique_categories = {category['category'] for category in operations}
    category_amount = {amount: 0 for amount in unique_categories}
    for category in operations:
        category_amount[category['category']] += category['amount']
    return max(category_amount, key=lambda x: category_amount[x])


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

    encrypt_symbols = [str(x) for x in range(10)]
    encrypt_category = ['passport_code', 'phone_number']
    keys = info.keys()
    for key in keys:
        for category in encrypt_category:
            if key == category:
                secure = ""
                for symbol in info[category]:
                    if symbol in encrypt_symbols:
                        secure += '*'
                    else:
                        secure += symbol
                info[key] = secure
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
