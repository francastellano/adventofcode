import util.DataLoader


def load_data_numbers (path_numbers):
    data = util.DataLoader.DataFile(path_numbers)
    data.load_basic_list()
    numbers_bingo = data.list[0].split(",")

    data = util.DataLoader.DataFile(path_numbers)
    data.load_basic_list()
    return numbers_bingo


def load_data_cards(path_cards):
    data = util.DataLoader.DataFile(path_cards)
    data.load_basic_list()

    cards = {}
    cards_index = 0
    rows_index = 0
    for values in data.list:

        if cards_index not in cards:
            cards[cards_index] = {}

        values = values.strip()
        if values == "":
            cards_index += 1
            rows_index = 0
        else:
            values = values.replace("  ", " ")
            values = values.split(" ")
            idx_col = 0
            for val in values:
                if rows_index not in cards[cards_index]:
                    cards[cards_index][rows_index] = {}
                cards[cards_index][rows_index][idx_col] = val
                idx_col += 1

            rows_index += 1

    return cards


def clean_number (data_cards, number_to_clean):

    for card in data_cards:
        #        print (f"card [{card}]")
        for row in data_cards[card]:
            # print(f"==> row [{row}]")
            for col in data_cards[card][row]:
                if data_cards[card][row][col] == number_to_clean:
                    data_cards[card][row][col] = None

    return data_cards


def get_winner (data_cards):

    number_of_rows = len(data_cards[0][1])

    for card in data_cards:

        for row in range(0, number_of_rows):
            number_nones = 0
            for col in range(0, number_of_rows):
                if data_cards[card][row][col] is None:
                    number_nones += 1

                if number_nones == number_of_rows:
                    return card

        for col in range(0,number_of_rows):
            number_nones = 0
            for row in range(0,number_of_rows):
                if data_cards[card][col][row] is None:
                    number_nones += 1

                if number_nones == number_of_rows:
                    return card

    return None


def calculate_cards(card):
    # print (card)
    number_of_rows = len(card[1])

    total = 0

    for row in range(0, number_of_rows):
        for col in range(0, number_of_rows):
            if card[col][row] is not None:
                total = total + int(card[col][row])

    return total


def main():
    path_file_numbers = "./2021/Day4/numbers.data"
    path_file_cards = "./2021/Day4/cards.data"

    data_numbers = load_data_numbers(path_file_numbers)
    data_cards = load_data_cards (path_file_cards)

    card_winner = None
    last_number = None

    for data in data_numbers:
        last_number = int(data)
        print (f"Evaluating the number [{data}]")
        data_cards = clean_number (data_cards, data)

        card_winner = get_winner(data_cards)
        if card_winner is not None:
            print (f"El card winner es {card_winner}")
            # print (data_cards[card_winner])
            break

    total = calculate_cards(data_cards[card_winner])
    print (f"Total = {total} last_number {last_number}  = {total * last_number}")


main()