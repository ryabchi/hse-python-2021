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
        if operation['category'] in cats:
            cats[operation['category']] += operation['amount']
        else:
            cats[operation['category']] = operation['amount']
    print(cats)
    for cat in cats:
        if max_cat_amount < cats[cat]:
            max_cat = cat
            max_cat_amount = cats[cat]
    return max_cat


def hide_personal_info(info: Dict[str, Any]) -> Dict[str, Any]:
    new_str = ''
    if 'passport_code' in info:
        tmp_len = len(info['passport_code'])
        tmp_str = info['passport_code']
        for num in tmp_str:
            if num == ' ':
                new_str += ' '
            elif num == '+':
                new_str += '+'
            else: new_str += '*'
        info['passport_code'] = new_str
        new_str = ''
    if 'phone_number' in info:
        tmp_len = len(info['phone_number'])
        tmp_str = info['phone_number']
        for num in tmp_str:
            if num == ' ':
                new_str += ' '
            elif num == '+':
                new_str += '+'
            else: new_str += '*'
        info['phone_number'] = new_str
        new_str = ''
    return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
