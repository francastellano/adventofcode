import util.DataLoader
import util.UtilVector

from util import UtilMatrix


def load_data (path_data):
    vectors = []
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()

    for row in data.list:
        (post_from, post_to) = row.split ("->")
        post_from = post_from.strip()
        post_to = post_to.strip()

        vector = util.UtilVector.UtilVector()
        (vector.from_x, vector.from_y) = post_from.split(",")
        (vector.to_x, vector.to_y) = post_to.split(",")

        vector.from_x = int(vector.from_x)
        vector.from_y = int(vector.from_y)

        vector.to_x = int(vector.to_x)
        vector.to_y = int(vector.to_y)

        vectors.append(vector)

    return vectors


def add_matrix (final_results, points):

    for row in points:
        for col in points[row]:
            final_results = UtilMatrix.add_value_matrix(final_results, row, col, 1)

    return final_results


def count_great_than (final_results, value):
    counter = 0
    for row in final_results:
        for col in final_results[row]:
            if final_results[row][col] >= value:
                counter += 1
    return counter


def main():
    path_data = "./2021/Day5/day5.data"

    vectors = load_data(path_data)

    final_results = {}

    for vector in vectors:
        vector.get_vector_type()
        points = vector.iterate_vector()

        final_results = add_matrix (final_results, points)

    number_of_points = count_great_than(final_results, 2)
    print (f"number_of_points: [{number_of_points}]")


main()
