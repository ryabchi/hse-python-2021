from typing import List, Dict, Any


def filter_list(numbers: List[int]) -> List[int]:
    new_list = []
    for num in numbers:
        if not (num % 2 == 0):
            new_list.append(num)
    return new_list


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    for cat in operations:
        if max_cat < cat['amount']:
            max_cat = cat
    return max_cat


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
    for client in info:
        if client['passport_code'] in info:
            for num in client['passport_code']:
                num = '*'
        if client['phone_number'] in info:
            for num in client['phone_number']:
                num = '*'
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
