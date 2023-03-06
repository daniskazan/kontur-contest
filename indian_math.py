from itertools import permutations
from functools import reduce


def main():
    data = []
    perms = list(permutations(input()))
    for perm in perms:
        data.append(int(reduce(lambda x, y: x + y, perm)))  # tuple ("6", "1", "7", "4") -> int: 6174

    v_max, v_min = max(data), min(data)
    print(v_max - v_min)


if __name__ == '__main__':
    main()