
def set_value_matrix(matrix, x, y, value):
    if x not in matrix:
        matrix[x] = {}

    if y not in matrix[x]:
        matrix[x][y] = None

    matrix[x][y] = value

    return matrix


def add_value_matrix(matrix, x, y, value):
    if x not in matrix:
        matrix[x] = {}

    if y not in matrix[x]:
        matrix[x][y] = 0

    matrix[x][y] = matrix[x][y] + value

    return matrix
