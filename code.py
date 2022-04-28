A = ((4.855, 1.239, 0.272, 0.258),
     (1.491, 4.954, 0.124, 0.236),
     (0.456, 0.285, 4.354, 0.254),
     (0.412, 0.335, 0.158, 2.874))


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


print(check_diagonal_advantage(A))
