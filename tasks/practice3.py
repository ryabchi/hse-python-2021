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
    return []
    return [x for x in numbers if x % 2 != 0]


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
    return ''
    list_categories = {category['category'] for category in operations}
    amount_category = {amount: 0 for amount in list_categories}
    for category in operations:
        amount_category[category['category']] += category['amount']
    return max(amount_category, key=lambda x: amount_category[x])


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
    symbols_to_encrypt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    category_to_encrypt = ['passport_code', 'phone_number']
    keys = info.keys()
    for key in keys:
        for cat in category_to_encrypt:
            if key == cat:
                secure = ""
                for symbol in info[cat]:
                    if symbol in symbols_to_encrypt:
                        secure += '*'
                    else:
                        secure += symbol
                info[key] = secure
    return info


def main() -> None:
    pass
if __name__ == '__main__':
    main()