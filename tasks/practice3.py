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
    nums = [x for x in numbers if x % 2 == 1]
    return nums


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """
    popular_category = ''
    max_amount = 0
    for i in operations:
        if i['amount'] > max_amount:
            max_amount = i['amount']
            popular_category = i['category']

    return popular_category


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

    if 'passport_code' in info:
        new_code = ''
        for i in info['passport_code']:
            if i >='0' and i <='9':
                new_code += '*'
            else:
                new_code += i
        info['passport_code'] = new_code
    if 'phone_number' in info:
        new_code = ''
        for i in info['phone_number']:
            if i >= '0' and i <= '9':
                new_code += '*'
            else:
                new_code += i
        info['phone_number'] = new_code

    return info


def main() -> None:
    print(filter_list([1, 2, 3, 4, 5]))
    print(get_popular_category([{'category': 'food', 'amount': 10}, {'category': 'cloth', 'amount': 12}]))
    print(hide_personal_info({'passport_code': '45673 562', 'phone_number': '+79567459137', 'fio': 'rgidggdid'}))


if __name__ == '__main__':
    main()
