import util.DataLoader


def get_data(path_file):
    data = util.DataLoader.DataFile(path_file)
    data.load_basic_list()

    return data.list


def accumulate (list_values):
    position = {}
    idx_position = 0
    for val in list_values:
        idx_character = 0

        for character_bin in val:

            if idx_character not in position:
                position[idx_character] = {}
                position[idx_character]["0"] = 0
                position[idx_character]["1"] = 0

            position[idx_character][character_bin] = position[idx_character][character_bin] + 1
            idx_character += 1

        idx_position += 1

    print (position)
    return position


def cal_gamma_rate2 (list_positions):
    return cal_generic_rate (list_positions, "0", "1")


def cal_epsilon_rate2 (list_positions):
    return cal_generic_rate (list_positions, "1", "0")


def cal_generic_rate(list_positions, value_mayor, value_minor):
    value = ""
    for row in list_positions:
        if list_positions[row][value_mayor] > list_positions[row][value_minor]:
            value = value + "0"
        else:
            value = value + "1"

    return value


def main():
    path_file = "./2021/Day3/day3.data"
    list_values = get_data(path_file)
    list_values_computed = accumulate(list_values)

    gama_rate = cal_gamma_rate2(list_values_computed)
    epsilon_rate = cal_epsilon_rate2(list_values_computed)

    decimal_gama_rate = int(gama_rate, 2)
    decimal_epsilon_rate = int(epsilon_rate, 2)

    print (decimal_gama_rate, decimal_epsilon_rate)

    print(decimal_gama_rate * decimal_epsilon_rate)

main()

# => 2035764
