import util.DataLoader


def load_data(path_data):
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()

    matrix_data = {}

    row_idx = 0
    for row in data.list:
        matrix_data[row_idx] = {}
        col_idx = 0
        for value in row:
            matrix_data[row_idx][col_idx] = value
            col_idx += 1

        row_idx += 1

    return matrix_data


def valida_position(data, row, col):
    if row != 0:
        if data[row][col] >= data[row - 1][col]:
            return False

    if col != 0:
        if data[row][col] >= data[row][col - 1]:
            return False

    if row != len(data) - 1:
        if data[row][col] >= data[row + 1][col]:
            return False

    if col != len(data[row]) - 1:
        if data[row][col] >= data[row][col+1]:
            return False

    return True


def main():
    path_data = "./2021/Day9/Day9.data"
    data_to_process = load_data(path_data)
    total_values = 0

    for row in data_to_process:
        for col in data_to_process[row]:

            if valida_position (data_to_process, row, col):
                total_values = total_values + int(data_to_process[row][col]) + 1

    print (f"Total number of values {total_values}")


main()


