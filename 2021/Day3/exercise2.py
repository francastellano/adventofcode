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

    return position


def filter_rows(rows, position, function_eval):

    if len(rows) == 1:
        return rows

    if function_eval == max:
        value_equal = "1"
    else:
        value_equal = "0"

    accumulated = accumulate (rows)

    if accumulated[position]["0"] == accumulated[position]["1"]:
        print (f"Equal {value_equal}")
        value_to_filter = value_equal
    elif function_eval(accumulated[position]["0"], accumulated[position]["1"]) == accumulated[position]["1"] :
        value_to_filter = "1"
    else:
        value_to_filter = "0"

    print (f"Value to fitler in postion {position} with data {accumulated[position]} is {value_to_filter}")

    rows_filtered = []
    for row in rows:
        if row[position] == value_to_filter:
            rows_filtered.append(row)

    return rows_filtered


def main():
    path_file = "./2021/Day3/day3.data"
    list_values_original = get_data(path_file)
    lit_values_calc = list_values_original

    length_for = len(lit_values_calc[0])

    for i in range(0,length_for):
        lit_values_calc = filter_rows (lit_values_calc, i, max)

    oxygen_generator_rating = (int (lit_values_calc[0], 2))

    lit_values_calc = list_values_original

    for i in range(0,length_for):
        lit_values_calc = filter_rows (lit_values_calc, i, min)

    co2_scrubber_rating = (int (lit_values_calc[0], 2))

    print (f"oxygen_generator_rating {oxygen_generator_rating}")
    print (f"co2_scrubber_rating {co2_scrubber_rating}")

    print (f"final calculation {oxygen_generator_rating * co2_scrubber_rating }")



main()
