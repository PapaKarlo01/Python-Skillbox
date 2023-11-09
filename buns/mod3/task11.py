a = []
while True:
    try:
        a.append(' '.join(input()).split(' '))
    except EOFError:
        break


def transponing(matrix):
    tMatrix = [[0 for n in range(1, len(a) + 1)] for k in range(len(a))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            tMatrix[i][j] = matrix[j][i]
    return tMatrix


def main_diagonal_check(matrix, sign):
    j = 0
    for i in range(0, len(matrix)):
        if matrix[i][j] != sign:
            return False
        j += 1
    return True


def second_diagonal_check(matrix, sign):
    j = len(matrix) - 1
    for i in range(0, len(matrix)):
        if matrix[i][j] != sign:
            return False
        j -= 1
    return True


def win(sign, matrix):
    for i in range(len(matrix)):
        if (matrix[i].count(sign) == len(a) or
                transponing(matrix)[i].count(sign) == len(a)) or main_diagonal_check(matrix, sign)\
                or second_diagonal_check(matrix, sign):
            return True
    return False


if win('X', a):
    print('X')
elif(win('O', a)):
    print('O')
else:
    print('Ничья')
