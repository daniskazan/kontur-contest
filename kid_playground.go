package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}

	rows, cols := len(matrix), len(matrix[0])
	heights := make([]int, cols)
	maxArea := 0

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if matrix[i][j] == '.' {
				heights[j] += 1
			} else {
				heights[j] = 0
			}
		}

		stack := make([]int, 0, cols+1)
		for j := 0; j < cols+1; j++ {
			for len(stack) > 0 && (j == cols || heights[stack[len(stack)-1]] > heights[j]) {
				height := heights[stack[len(stack)-1]]
				stack = stack[:len(stack)-1]
				width := j
				if len(stack) > 0 {
					width = j - stack[len(stack)-1] - 1
				}
				area := height * width
				if area > maxArea {
					maxArea = area
				}
			}
			stack = append(stack, j)
		}
	}

	return maxArea
}

func main() {
	// Create a new scanner that reads from os.Stdin
	scanner := bufio.NewScanner(os.Stdin)

	// Read the first line containing n and m
	scanner.Scan()
	line := scanner.Text()
	parts := strings.Split(line, " ")
	n, _ := strconv.Atoi(parts[0])

	// Read the remaining n lines containing the matrix
	matrix := make([][]byte, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		matrix[i] = []byte(scanner.Text())
	}
	fmt.Println(maximalRectangle(matrix))
}
