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
    print(r"max{", end='')
    print(*[round(sum(map(abs, line)), 6) for line in matrix], sep=', ', end='')
    print(r'}')
    return max([sum(map(abs, line)) for line in matrix])


def choose_criterion(q):
    """Takes q and returns a stopping criterion"""
    if q <= 0.5:
        return lambda x1, x0, eps: max(map(lambda x, y: abs(x - y), x1, x0)) < eps
    return lambda x1, x0, eps: q / (1 - q) * max(map(lambda x, y: abs(x - y), x1, x0)) < eps


def next_term(B, c, x0):
    """Takes matrix of coefficients and free terms of equation x = Bx + c and previous term, returns next term"""
    x1 = tuple(round(sum([B[i][j] * x0[j if j < i else j + 1] for j in range(len(B[i]))]) + c[i][0], 6) for i in
               range(len(x0)))
    return x1


def find_root(criterion, B, c, x0, eps):
    """Finds root of system of linear algebraic equations
    Takes:
        criterion - criterion of stopping
        B, c - matrix of coefficients and free terms of equation x = Bx + c
        x0 - initial approximation
        eps - precision
    Return:
        x1 - root of system of linear algebraic equations
        log - history of approximations
    """
    log = [x0]
    x1 = next_term(B, c, x0)
    log.append(x1)
    while not criterion(x1, x0, eps):
        x0 = x1
        x1 = next_term(B, c, x0)
        log.append(x1)
    return x1, log


def print_matrix(matrix):
    """Takes matrix and print it to the stdout"""
    for line in matrix:
        for num in line:
            print(str(num).ljust(10), end=' ')
        print()


def print_matrix_equation(A, b):
    """Takes matrix of coefficients and free terms of equation Ax = b and print this equation"""
    for i in range(len(A)):
        s = [str(A[i][j]) + f'∙x{j + 1}' for j in range(len(A[i]))]
        print(' + '.join(s) + ' = ' + str(b[i]))


def print_trans_equation(B, c):
    """Takes matrix of coefficients and free terms of equation x = Bx + c and print this equation"""
    for i in range(len(B)):
        s = [str(B[i][j]) + f'∙x{j + 1 if j < i else j + 2}' for j in range(len(B[i]))]
        print(f'x{i + 1} = ' + ' + '.join(s) + ' + ' + str(*c[i]))


def print_log(log):
    print("-"*89)
    print('|' + "№ iteration".center(15) + '|' +
          "|".join([f"x{i + 1}".center(12) for i in range(len(log[0]))]) + "|" +
          "||x^k - x^k-1||".center(19) + "|")
    print("-" * 89)
    for i in range(len(log)):
        print('|' + f"{i}".center(15) + '|' +
              "|".join([str(x).center(12) for x in log[i]]) + "|" +
              str(round(max(map(lambda x, y: abs(x - y), log[i], log[i-1])), 6) if i > 0 else 0).center(19) + "|")
        print("-" * 89)


# Lab steps

# Print input data
print('Initial data:')
print_matrix_equation(A, b)
print()

# Check diagonal advantage
print('Checking diagonal advantage:')
print('Result:', check_diagonal_advantage(A), '\n')

# Transform equation from Ax = b to x = Bx + c
print("Transforming equation from Ax = b to x = Bx + c:")
B, c = highlight_root(A, b)
print_trans_equation(B, c)
print()

# Find matrix norm
print("Calculating matrix norm:")
q = matrix_norm(B)
print('Result:', q, '\n')

# Put c as an initial approximation
print('Put c as an initial approximation')
x = tuple(n[0] for n in c)
print(f'x0 = {x}\n')

# Choose stopping criterion
print("Choosing stopping criterion:")
criterion = choose_criterion(q)
print(f"q = {q}")
if q <= 0.5:
    print("Criterion:||x^k - x^k-1||≤ ε")
else:
    print("Criterion: (q/1−q) * ||x^k - x^k-1||≤ ε")

# Searching for root
print("\nCalculating root:")
x, log = find_root(criterion, B, c, x, 0.00001)
print_log(log)
print("Result:", x)

