def diagonal_difference(arr):
    n = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n-i-1]

    return abs(primary_diagonal - secondary_diagonal)

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
result = diagonal_difference(arr)
print(result)  # Output: 15








