import util.DataLoader


def get_list(path_file):
    data = util.DataLoader.DataFile(path_file)
    data.load_basic_number_list()

    return data.list


def pre_compute_list (list_of_values_to_compute):
    final_list = []

    for idx, val in enumerate(list_of_values_to_compute):
        if idx not in (0, 1):
            value_to_add = list_of_values_to_compute[idx] + \
                           list_of_values_to_compute[idx-1] + \
                           list_of_values_to_compute[idx-2]
            final_list.append(value_to_add)

    return final_list


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
    list_values_no_computed = get_list(path_file)
    list_values = pre_compute_list(list_values_no_computed)

    print(len(list_values_no_computed))
    print (len(list_values))
    exercise1(list_values)


main()
