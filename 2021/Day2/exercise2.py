import util.DataLoader


def get_data(path_file):
    data = util.DataLoader.DataFile(path_file)
    data.load_basic_list()

    return data.list


def calc_aim(aim, movement_type, movement_value):
    if movement_type == "forward":
        return aim

    if movement_type == "up":
        return aim - movement_value

    if movement_type == "down":
        return aim + movement_value

    raise


def calculate_position(list_values):

    aim = 0
    forward = 0
    depth = 0

    for value in list_values:
        (movement_type, movement_value) = value.split(" ")
        movement_value = int (movement_value)

        aim = calc_aim(aim, movement_type, movement_value)

        if movement_type == "forward":
            forward = forward + movement_value
            depth = depth + (aim * movement_value)

    print (f"forward [{forward}] depth [{depth}]")
    print (f"Final result {forward * depth}")


def main():
    path_file = "./2021/Day2/day2.data"
    list_values = get_data(path_file)

    calculate_position(list_values)


main()

