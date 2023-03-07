import typing as t

def maximalRectangle(matrix: t.List[t.List[str]]):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '.':
                heights[j] += 1
            else:
                heights[j] = 0

        stack = []
        for j in range(cols + 1):
            while stack and (j == cols or heights[stack[-1]] > heights[j]):
                height = heights[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(j)

    return max_area


def main():
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(input()))

    return maximalRectangle(matrix=data)


if __name__ == '__main__':
    print(main())