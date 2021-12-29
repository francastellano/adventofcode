import util.DataLoader


def calc_result(path):
    return 7


def exercise1(path):

    data = util.DataLoader.DataFile(path)

    data.load_basic_number_list()
    result = 0
    previous_result = None

    for idx, val in enumerate(data.list):

        if previous_result is not None:
            if val > previous_result:
                result += 1

        previous_result = val

    print (f"The final result is {result}")


path = "./2021/Day1/exercise1.data"
exercise1(path)
