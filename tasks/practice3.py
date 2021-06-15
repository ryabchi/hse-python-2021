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
    numbers2 = [x for x in numbers if x % 2 != 0]
    # впишите ваш код здесь
    return numbers2


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
    amounts = [x.get('amount') for x in operations]
    max_index = amounts.index(max(amounts))
    return operations[max_index].get('category')


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
    for key in info:
        if key == 'passport_code' or key == 'phone_number':
            new_info = ''
            for symbol in info[key]:
                if symbol in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    new_info += '*'
                else:
                    new_info += symbol
            info.update({key: new_info})
    return info


def main() -> None:
    l=[1,2,3,4,5,6,7,8,89,0]
    print(filter_list(l))
    a = [{'category': 'название категории', 'amount': 100}, {'category': 'категории', 'amount': 200}, {'category': 'название', 'amount': 50}]
    print(get_popular_category(a))
    print(hide_personal_info({'name': 'Mike', 'passport_code': '68416841', 'phone_number': '927946849864'}))
    pass


if __name__ == '__main__':
    main()