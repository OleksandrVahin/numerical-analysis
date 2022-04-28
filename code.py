A = ((4.855, 1.239, 0.272, 0.258),
     (1.491, 4.954, 0.124, 0.236),
     (0.456, 0.285, 4.354, 0.254),
     (0.412, 0.335, 0.158, 2.874))

B1 = (1.192, 0.256, 0.852, 0.862)


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


def highlight_root(A, B):
    """Takes two matrices(A, B from Ax = B) and returns two matrices(B, C from x = Bx + C)"""
    new_B = []
    C = []
    for i in range(len(A)):
        new_B.append(tuple(round(-n / A[i][i], 6) for n in A[i][:i] + A[i][i + 1:]))
        C.append((round(B[i] / A[i][i], 6), ))
    return tuple(new_B), tuple(C)


def print_matrix(matrix):
    """Takes matrix and print it to the stdout"""
    for line in matrix:
        for num in line:
            print(str(num).ljust(10), end=' ')
        print()




print(check_diagonal_advantage(A))
B2, C = highlight_root(A, B1)
print_matrix(B2)
print_matrix(C)