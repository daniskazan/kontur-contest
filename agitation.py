from typing import Tuple, List, Dict
from collections import defaultdict
import re

def split_address(s: str) -> Tuple[str, int]:
    match = re.search(r'\d', s)
    if match is None:
        return s, 0
    else:
        index = match.start()
        non_numeric = s[:index]
        numeric = int(s[index:])
        return non_numeric, numeric



def take_input() -> Tuple[List, Dict]:
    already_visited = defaultdict(set)
    n = int(input())

    for _ in range(n):
        street, home_numb = split_address(input())
        already_visited[street].add(home_numb)

    m = int(input())
    streets_to_visit = [input() for _ in range(m)]
    return streets_to_visit, already_visited


def main():
    res = []
    streets_to_visit, already_visited = take_input()
    for street in streets_to_visit:
        for i in range(1, 1000001):
            if i not in already_visited[street]:
                res.append(i)
                already_visited[street].add(i)
                break
            else:
                continue
    return res


if __name__ == '__main__':
    print(*main())
