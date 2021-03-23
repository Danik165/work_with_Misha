import numpy as np

"Какой-то массив из блокнота"
game_zone = np.array([
    ['_', '_', '_', '_'],
    ['*', '_', '_', '_'],
    ['_', '*', '_', '_'],
    ['_', '_', '*', '_'],
    ['_', '_', '_', '_'],
])


def detect_alive_block(field):
    for i in range(0, field.shape[0]):
        for j in range(0, field.shape[1]):
            if field[i][j] == '*':
                middle_elem = field[i + 1][i + 1]
                return field[i:i + 3, j:j + 3]


def print_matrix(matrix):
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            print(matrix[i][j], end=' ')
        print()


print_matrix(detect_alive_block(game_zone))


def step(matrix, neighbours=0):
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            if matrix[i][j] == '*':
                neighbours += 1
    if (matrix[1][1] == '*') and (neighbours < 3 or neighbours > 5):
        matrix[1][1] = '_'
    elif (matrix[1][1] == '_') and (neighbours == 3):
        matrix[1][1] = '*'

    return matrix


print_matrix(step(detect_alive_block(game_zone)))

#         "Таймер где-то тут"
