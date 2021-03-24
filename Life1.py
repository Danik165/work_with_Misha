import numpy as np

"Какой-то массив из блокнота"
game_zone = np.array([
    ['_', '_', '_', '_'],
    ['_', '*', '*', '_'],
    ['_', '*', '*', '_'],
    ['_', '*', '*', '_'],
    ['_', '_', '_', '_'],
])


def print_matrix(matrix):
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            print(matrix[i][j], end=' ')
        print()
    print('_______')


def step(matrix, neighbours=0):
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            if matrix[i][j] == '*':
                neighbours += 1
    if (matrix[1][1] == '*') and (neighbours < 3 or neighbours > 4):
        matrix[1][1] = '_'
    elif (matrix[1][1] == '_') and (neighbours == 3):
        matrix[1][1] = '*'

    return matrix


def detect_alive_block(field):
    for i in range(1, field.shape[0] - 1):
        for j in range(1, field.shape[1] - 1):
            print_matrix(step(field[i - 1:i + 2, j - 1:j + 2]))


"если убрать тут step, то будет обычный вывод матрицы 3х3"




"Печать первого живого блока"
print_matrix(detect_alive_block(game_zone))

"Полная печать"


def life(opperations):
    pass
    while opperations > 0:
        print_matrix(step(detect_alive_block(game_zone)))
        opperations -= 1


#life(int(input()))
#         "Таймер где-то тут"
