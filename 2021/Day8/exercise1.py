import util.DataLoader


def load_data(path_data):
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()

    results = {}
    idx = 0

    for value in data.list:
        results[idx] = value.split('|')

        results[idx][0] = results[idx][0].strip().split(" ")
        results[idx][1] = results[idx][1].strip().split(" ")
        idx += 1

    return results


def process_digits(digit):
    if len(digit) == 2:
        return 1
    if len(digit) == 3:
        return 7
    if len(digit) == 4:
        return 4
    if len(digit) == 7:
        return 8

    return None


def process_row(values):
    print (values)
    count_digi = 0
    for value in values:

        if process_digits(value) in (1, 4, 7, 8):
            count_digi += 1

    return count_digi


def main():
    path_data = "./2021/Day8/day8.data"
    data_to_process = load_data(path_data)

    count_digi = 0
    for row in data_to_process:
        count_digi = count_digi + process_row (data_to_process[row][1])

    print (count_digi)


main()