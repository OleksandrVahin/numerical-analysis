A = ((4.855, 1.239, 0.272, 0.258),
     (1.491, 4.954, 0.124, 0.236),
     (0.456, 0.285, 4.354, 0.254),
     (0.412, 0.335, 0.158, 2.874))

b = (1.192, 0.256, 0.852, 0.862)


def check_diagonal_advantage(matrix):
    """Takes square matrix, returns True if matrix has a diagonal advantage, else False"""
    check_line = []
    for i in range(len(matrix)):
        line = tuple(map(abs, matrix[i]))
        check_line.append(line[i] > sum(line[:i] + line[i + 1:]))
        s = f'|{matrix[i][i]}| {">" if check_line[-1] else "<"} ' + " + ".join(
            [f'|{n}|' for n in matrix[i][:i] + matrix[i][i + 1:]])
        print(s)
    return all(check_line)


def highlight_root(A, b):
    """Takes two matrices(A, B from Ax = b) and returns two matrices(B, C from x = Bx + c)"""
    B = []
    c = []
    for i in range(len(A)):
        B.append(tuple(round(-n / A[i][i], 6) for n in A[i][:i] + A[i][i + 1:]))
        c.append((round(b[i] / A[i][i], 6),))
    return tuple(B), tuple(c)


def matrix_norm(matrix):
    """Takes matrix, return matrix norm(maximum of sum's of absolutes of each line)"""
    return max([sum(map(abs, line)) for line in matrix])


def print_matrix(matrix):
    """Takes matrix and print it to the stdout"""
    for line in matrix:
        for num in line:
            print(str(num).ljust(10), end=' ')
        print()


def print_matrix_equation(A, b):
    """Takes matrix of coefficients and free terms of equation Ax = b and print this equation"""
    for i in range(len(A)):
        s = []
        for j in range(len(A[i])):
            s.append(str(A[i][j]) + f'∙x{j + 1}')
        print(' + '.join(s) + ' = ' + str(b[i]))


# Lab steps

# Print input data
print('Initial data:')
print_matrix_equation(A, b)
print()

# Check diagonal advantage
print('Checking diagonal advantage:')
print('Result:', check_diagonal_advantage(A), '\n')

# Transform equation from Ax = b to x = Bx + c
B, c = highlight_root(A, b)
print_matrix(B)
print_matrix(c)
print(matrix_norm(B))
