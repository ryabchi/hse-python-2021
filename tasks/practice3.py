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

    return [x for x in numbers if (x % 2 != 0)]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    comb_of_operations = {}
    max_amount = 0
    for operation in operations:
        if operation.get('category') not in comb_of_operations:
            comb_of_operations[operation.get('category')] = 1
        else:
            comb_of_operations[operation.get('category')] += 1
    for operation in comb_of_operations:
        if comb_of_operations.get(operation) > max_amount:
            max_amount = comb_of_operations.get(operation)
            string = operation
    return string


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

    for key in info:
        if key == 'passport_code' or key == 'phone_number':
            new_info = ''
            for letter in info[key]:
                if letter in ['0','1','2','3','4','5','6','7','8','9']:
                    new_info += '*'
                else:
                    new_info += letter
            info.update({key: new_info})
    return info


def main() -> None:
    """"
    print(filter_list([1, 2, 3, 4, 5]))
    print(get_popular_category([{'category': 'супермаркеты', 'amount': 3680}, {'category': 'рестораны', 'amount': 4649},
    {'category': 'супермаркеты', 'amount': 1388}, {'category': 'рестораны', 'amount': 1566},
    {'category': 'дом, ремонт', 'amount': 646}, {'category': 'дом, ремонт', 'amount': 4524},
    {'category': 'дом, ремонт', 'amount': 2751}, {'category': 'супермаркеты', 'amount': 1411},
    {'category': 'рестораны', 'amount': 2140}, {'category': 'рестораны', 'amount': 3672},
    {'category': 'рестораны', 'amount': 31}, {'category': 'дом, ремонт', 'amount': 1592},
    {'category': 'рестораны', 'amount': 1514}, {'category': 'транспорт', 'amount': 457},
    {'category': 'транспорт', 'amount': 577}, {'category': 'дом, ремонт', 'amount': 1799},
    {'category': 'транспорт', 'amount': 3271}]))
    print(hide_personal_info({'name': 'Jhon', 'passport_code': '2200 775511', 'phone_number': '+78005553535'}))
    """
    pass


if __name__ == '__main__':
    main()
