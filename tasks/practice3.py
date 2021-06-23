from typing import List, Dict, Any

import re

def filter_list(numbers: List[int]) -> List[int]:

    return [i for i in numbers if i % 2 != 0]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:


    caty = {i:0 for i in [j['category'] for j in operations]}

    for i in operations:
        caty[i['category']] += i['amount']

    return max(caty, key=lambda x: caty[x])

def hide_personal_info(info: Dict[str, Any]) -> Dict[str, Any]:
 

    return {key: re.sub(r'[0-9]', "*", value) for key, value in info.items()}

def main() -> None:
    print(get_popular_category([{'category': 'супермаркеты', 'amount': 3380}, {'category': 'рестораны', 'amount': 5649}]))

if __name__ == '__main__':
    main()
