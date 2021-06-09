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

    set_oper = set(i['category'] for i in operations)
    clean_oper = {i: 0 for i in set_oper}
    for i in operations:
        clean_oper[i['category']] += i['amount']
    return max(clean_oper, key=lambda x: clean_oper[x])


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


    nums = ['1','2','3','4','5','6','7','8','9','0']
    key_list = info.keys()
    categ_to_encrypt = ['passport_code', 'phone_number']
    for i in categ_to_encrypt:
        if i in key_list:
            info[i] = ''.join('*' if j in nums else j for j in info[i])
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
