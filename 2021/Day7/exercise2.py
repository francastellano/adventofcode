import util.DataLoader
import time

def load_data(path_data):
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()
    values = data.list[0]
    values = values.split(',')
    return values


def accumulate_positions (matrix):

    accumulated = {}
    for position in matrix:
        position = int (position)
        if position not in accumulated:
            accumulated[position] = 0

        accumulated[position] = accumulated[position] + 1

    return accumulated


def get_max_and_min (accumulated):

    pos_max = None
    pos_min = None

    for pos in accumulated:
        if pos_max is None:
            pos_max = pos
            pos_min = pos
        else:
            pos_max = max(pos_max, pos)
            pos_min = min(pos_min, pos)

    return pos_min, pos_max


def get_position_with_min_cost (results):
    min_cost = None
    idx = None
    for res in results:
        if min_cost is None:
            min_cost = results[res]
            idx = res
        elif min_cost > results[res]:
            min_cost = results[res]
            idx = res

    return idx


def main():
    path_data = "./2021/Day7/day7.data"
    positions = load_data(path_data)

    data_accumulated = accumulate_positions(positions)

    results = {}

    (pos_min, pos_max) = get_max_and_min(data_accumulated)

    print(f'(pos_min, pos_max) => ({pos_min}, {pos_max})')
    print ("Calculation the positions ....")

    for pos in range (pos_min, pos_max + 1):
        # print(f"Calculating the position {pos} ...")
        fuel_cost = 0

        for data in data_accumulated:
            movements = abs(data - pos)
            cost = 1
            movement_cost = 0
            for move_cost in range (0, movements):
                movement_cost = movement_cost + (cost * data_accumulated[data])
                cost += 1

            fuel_cost = fuel_cost + movement_cost

        results[pos] = fuel_cost

    print ("Getting the position with less cost ...")
    position = get_position_with_min_cost (results)

    print (f"The position {position} is the one with lest cost {results[position]}")


start = time.time()
main()
end = time.time()
print(end - start)