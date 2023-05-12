def init_matrix(rows, cols):
    return [['']*cols for _ in range(rows)]


def convert(s, n):
    string_length = len(s)

    if n == 1:
        return s

    # matrix = init_matrix(n, ((string_length // 2*(n-1)) + 1) * (n-1))
    matrix = init_matrix(n, string_length)

    string_index = 0
    matrix_column = 0
    while string_index < string_length:
        i = 0
        while i < n and string_index < string_length:
            matrix[i][matrix_column] = s[string_index]

            i += 1
            string_index += 1
        matrix_column += 1

        i = n - 2
        while i > 0 and string_index < string_length:
            matrix[i][matrix_column] = s[string_index]

            i -= 1
            string_index += 1
            matrix_column += 1

    return ''.join([''.join(row) for row in matrix])


if __name__ == "__main__":
    print(convert(s="PAYPALISHIRING", n=3))
