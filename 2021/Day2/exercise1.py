import util.DataLoader


def get_data(path_file):
    data = util.DataLoader.DataFile(path_file)
    data.load_basic_list()

    return data.list


def calculate_position(list_values):
    accumulated_movements = {}
    for value in list_values:
        value = value.split(" ")
        if value[0] not in accumulated_movements:
            accumulated_movements[value[0]] = 0

        accumulated_movements[value[0]] = accumulated_movements[value[0]] + int(value[1])

    depth = int (accumulated_movements["down"]) - int(accumulated_movements["up"])
    result = depth * accumulated_movements["forward"]

    print(f"The final position is depth: {depth} & forward { accumulated_movements['forward']}  = {result}")


def main():
    path_file = "./2021/Day2/day2.data"
    list_values = get_data(path_file)

    calculate_position(list_values)


main()
