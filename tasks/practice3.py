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
    odd_numbered_list = [x for x in numbers if x % 2 != 0]
    return odd_numbered_list


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
    priority_client_category = operations[0]
    for operation in operations:
        if operation['amount'] >= priority_client_category['amount']:
            priority_client_category = operation
    return priority_client_category['category']



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

    if 'passport_code' in info:
        protect_passport_code = str(info['passport_code'])
        for number in str(info['passport_code']):
             if number in {x for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}:
                protect_passport_code = protect_passport_code.replace(number, '*')
        info['passport_code'] = protect_passport_code
    if 'phone_number' in info:
        protect_phone_number = str(info['phone_number'])
        for number in str(info['phone_number']):
            if number in {x for x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}:
                protect_phone_number = protect_phone_number.replace(number, '*')
        info['phone_number'] = protect_phone_number
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
