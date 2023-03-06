
def main():
    data = []
    n = int(input())
    for _ in range(n):
        data.append(int(input()))

    return 0 - sum(data)


if __name__ == '__main__':
    print(main())
