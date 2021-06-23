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
            count[d['category']] = d['amount']
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
        newstr =''
        for x in info['passport_code']:
            if x.isdigit():
                newstr += '*'
            else:
                newstr += x
        info['passport_code'] = newstr      
    if 'phone_number' in info.keys():
        newstr =''
        for x in info['phone_number']:
            if x.isdigit():
                newstr += '*'
            else:
                newstr += x
        info['phone_number'] = newstr 
    return info


def main() -> None:
    pass
operations = [{'amount': 3680, 'category': 'супермаркеты'},
 {'amount': 4649, 'category': 'рестораны'},
 {'amount': 1388, 'category': 'супермаркеты'},
 {'amount': 1566, 'category': 'рестораны'},
 {'amount': 646, 'category': 'дом, ремонт'},
 {'amount': 4524, 'category': 'дом, ремонт'},
 {'amount': 2751, 'category': 'дом, ремонт'},
 {'amount': 1411, 'category': 'супермаркеты'},
 {'amount': 2140, 'category': 'рестораны'},
 {'amount': 3672, 'category': 'рестораны'},
 {'amount': 31, 'category': 'рестораны'},
 {'amount': 1592, 'category': 'дом, ремонт'},
 {'amount': 1514, 'category': 'рестораны'},
 {'amount': 457, 'category': 'транспорт'},
 {'amount': 577, 'category': 'транспорт'},
 {'amount': 1799, 'category': 'дом, ремонт'},
 {'amount': 3271, 'category': 'транспорт'}]
print(get_popular_category(operations))


if __name__ == '__main__':
    main()
