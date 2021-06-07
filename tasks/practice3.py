from typing import List, Dict, Any


def filter_list(numbers: List[int]) -> List[int]:
    new_list = []
    for num in numbers:
        if not (num % 2 == 0):
            new_list.append(num)
    return new_list


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    cats = dict()
    max_cat_amount = 0
    max_cat = ''
    for operation in operations:
        for cat in cats:
            if operation['category'] == cat['category']:
                cats['amount'] += operation['amount']
            else:
                cats[operation['category']] = operation['amount']
    for cat in cats:
        if max_cat_amount < cat['amount']:
            max_cat = cat['category']
    return max_cat


def hide_personal_info(info: Dict[str, Any]) -> Dict[str, Any]:
    new_str = ''
    for client in info:
        if 'passport_code' in client:
            tmp = len(str(client[passport_code]))
            for i in range(tmp):
                new_str += '*'
            client[passport_code] = new_str
        if 'phone_number' in client:
            tmp = len(str(client[phone_number]))
            for i in range(tmp):
                new_str += '*'
            client[phone_number] = new_str
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
