import util.DataLoader


def exercise1(path_file):

    data = util.DataLoader.DataFile(path_file)

    data.load_basic_number_list()
    result = 0
    previous_result = None

    for idx, val in enumerate(data.list):

        if previous_result is not None:
            if val > previous_result:
                result += 1

        previous_result = val

    print(f"The final result is {result}")


path = "./2021/Day1/exercise1.data"
exercise1(path)
