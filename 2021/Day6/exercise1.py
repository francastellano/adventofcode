import util.DataLoader


def load_data(path_data):
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()
    values = data.list[0]
    values = values.split (',')
    return values


def init_matrix():
    matrix = {}
    for x in range(0, 9):
        matrix[x] = 0

    return matrix


def accumulate_fishes_by_day(fishes):
    matrix_days = init_matrix()
    for fish in fishes:
        fish = int(fish)

        if fish not in matrix_days:
            matrix_days[fish] = 0
        matrix_days[fish] += 1

    return matrix_days


def next_day_calculations(fishes):
    matrix_days = init_matrix()

    for fish in fishes:
        if fish == 0:
            matrix_days[8] = matrix_days[8] + fishes[fish]
            matrix_days[6] = matrix_days[6] + fishes[fish]
        else:
            matrix_days[fish - 1] = matrix_days[fish - 1] + fishes[fish]

    return matrix_days


def count_fishes(fishes):
    fishes_number = 0
    for day in fishes:
        fishes_number = fishes_number + fishes[day]

    return fishes_number


def main():
    path_data = "./2021/Day6/day6.data"
    fishes = load_data(path_data)

    fishes = accumulate_fishes_by_day(fishes)

    days_to_check = 256

    for r in range(0, days_to_check):
        fishes = next_day_calculations(fishes)

    final_fishes = count_fishes(fishes)

    print(f"After {days_to_check} days there are {final_fishes} fishes.")


main()