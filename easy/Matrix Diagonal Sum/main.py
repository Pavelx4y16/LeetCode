def get_diagonals_sum(matrix):
    n = len(matrix)
    res = -matrix[n // 2][n // 2] if n % 2 else 0

    for i in range(n):
        res += matrix[i][i] + matrix[i][n-i-1]

    return res
