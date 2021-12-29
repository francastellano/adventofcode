import util.DataLoader


def get_list(path_file):
    data = util.DataLoader.DataFile(path_file)
    data.load_basic_number_list()

    return data.list


def exercise1(list_of_values_to_check):
    result = 0
    previous_result = None

    for idx, val in enumerate(list_of_values_to_check):

        if previous_result is not None:
            if val > previous_result:
                result += 1

        previous_result = val

    print(f"The final result is {result}")


def main():
    path_file = "./2021/Day1/exercise1.data"
    list_values = get_list(path_file)

    exercise1(list_values)


main()
