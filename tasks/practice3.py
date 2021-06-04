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
    numbers = [x for x in numbers if x % 2 == 1]
    return numbers


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
    set_operations = set(val['category'] for val in operations)
    cleaned_operations = {val: 0 for val in set_operations}
    for val in operations:
        cleaned_operations[val['category']] += val['amount']
    return max(cleaned_operations, key=lambda x: cleaned_operations[x])


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
    all_keys = info.keys()
    symbols_to_encrypt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    encrypting_pos = ['passport_code', 'phone_number']
    for pos in encrypting_pos:
        if pos in all_keys:
            info[pos] = ''.join('*' if j in symbols_to_encrypt else j for j in info[pos])
    print(info)
    return info


def main() -> None:
    hide_personal_info( {'name': 'Jhon', 'lastname': 'Doe', 'passport_code': '2200 775511', 'phone_number': '+78005553535'})


if __name__ == '__main__':
    main()
