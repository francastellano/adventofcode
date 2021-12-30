import util.DataLoader


def load_data(path_data):
    data = util.DataLoader.DataFile(path_data)
    data.load_basic_list()

    results = {}
    idx = 0

    for value in data.list:
        results[idx] = value.split('|')

        results[idx][0] = results[idx][0].strip().split(" ")
        results[idx][1] = results[idx][1].strip().split(" ")
        idx += 1

    return results


def process_digits(digit):
    if len(digit) == 2:
        return 1
    if len(digit) == 3:
        return 7
    if len(digit) == 4:
        return 4
    if len(digit) == 7:
        return 8

    return None


def find_by_length(list_values, length_to_find):
    for value in list_values:
        if len(value) == length_to_find:
            return value


def group_by_character (list_of_values):
    # Def get characters present

    matrix_char = {}

    for value in list_of_values:
        for letter in value:
            if letter not in matrix_char:
                matrix_char[letter] = 0

            matrix_char[letter] = matrix_char[letter] + 1

    return matrix_char


def replace_characters(character_to_be_cleaned, character_to_clean):
    for value in character_to_clean:
        character_to_be_cleaned = character_to_be_cleaned.replace(value, "")

    return character_to_be_cleaned


def find_non_order_pattern (list_to_be_checked, value_to_check):
    for value in list_to_be_checked:
        if sorted (value) ==  sorted(value_to_check):
            return value


def calc_values (pattern, values):
    #print (f"Revieing the values [{values}] in the pattern [{pattern}]")
    concat_value = ""
    for value in values:
        for pat in pattern:
            if sorted(value) == sorted(pattern[pat]):
                concat_value = concat_value + str(pat)

    return concat_value


def solve_pattern(pattern):
    # print (f"Solving the pattern {pattern}")
    matrix_results = {}
    matrix_characters = {}

    # Find the patterns by length
    matrix_results[1] = find_by_length (pattern, 2)
    pattern.remove(matrix_results[1])

    matrix_results[4] = find_by_length (pattern, 4)
    pattern.remove(matrix_results[4])

    matrix_results[7] = find_by_length (pattern, 3)
    pattern.remove(matrix_results[7])

    matrix_results[8] = find_by_length (pattern, 7)
    pattern.remove(matrix_results[8])

    # Group characters in the pending data
    matrix_chars_grouped = group_by_character(pattern)

    # Top character = characters present in 7 - 1
    matrix_characters[1] = replace_characters(matrix_results[7], matrix_results[1])

    # There are two characters that are present in the rest of the data
    # Top character is len = 6 one of them can be calculated: Characters 7 - Characters 1

    del matrix_chars_grouped[matrix_characters[1]]

    # The other that is present in all the remanding values is the digit
    for value in matrix_chars_grouped:
        if matrix_chars_grouped[value] == 6:
            matrix_characters[7] = value

    # Number 9 can now be constructed as: Number 4 + top character + down character
    matrix_results[9] = find_non_order_pattern(pattern, matrix_results[4] + matrix_characters[1] + matrix_characters[7])
    pattern.remove(matrix_results[9])

    # Character 5 = Characters of 8 - Characters of 9
    matrix_characters[5] = replace_characters(matrix_results[8], matrix_results[9])

    # We can set the character [down,left] as the one that is present in 1 & in the pending 5 patterns pending
    # to be processed.
    # The other with len = 5 is the middle character

    for value in matrix_chars_grouped:
        if matrix_chars_grouped[value] == 5:
            if value in matrix_results[1]:
                matrix_characters[6] = value
            else:
                matrix_characters[4] = value

    # Now that we have the middle lets find the 0 as characters in 8 - middle character
    matrix_results[0] = matrix_results[8].replace(matrix_characters[4], "")
    matrix_results[0] = find_non_order_pattern (pattern, matrix_results[0])
    pattern.remove(matrix_results[0])

    # Character top-right = characters in 1 - character number 6
    matrix_characters[3] = matrix_results[1].replace(matrix_characters[6], "")

    # Number 5 = Number 9 - character 3
    matrix_results[5] = matrix_results[9].replace(matrix_characters[3], "")
    matrix_results[5] = find_non_order_pattern (pattern, matrix_results[5])
    pattern.remove(matrix_results[5])

    # The other with length = 5 is the number 6
    matrix_results[6] = find_by_length (pattern, 6)
    pattern.remove(matrix_results[6])

    # We filter the rest by the character 6
    for value in pattern:
        if matrix_characters[5] in value:
            matrix_results[2] = value
        else:
            matrix_results[3] = value

    print (matrix_results)
    return matrix_results


def process_row(pattern, values):
    pat = solve_pattern(pattern)
    value = calc_values(pat, values)
    return value


def main():
    path_data = "./2021/Day8/day8.data"
    data_to_process = load_data(path_data)

    total_cal = 0
    for row in data_to_process:
        value =  process_row (data_to_process[row][0], data_to_process[row][1])
        total_cal = total_cal + int(value)

    print (f"El total es de {total_cal}")

main()