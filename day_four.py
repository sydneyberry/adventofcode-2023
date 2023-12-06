def part_one(input_file):
    line_list = input_file.readlines()
    length = len(line_list)

    card_totals = []
    running_total = 0

    for x, line in enumerate(line_list):
        running_total += get_card_total(line, x)

    return running_total


def get_card_total(line, x):
    print("LINE: " + line[:-1])
    card_total = 0
    # parse to colon
    start_index = line.find(":") + 2
    line = line[start_index:-1]
    split_line = line.split(" | ")
    winning_nums = split_line[0].split(" ")
    card_nums = split_line[1].split(" ")

    sum = 0

    for winning_num in winning_nums:
        if winning_num != " " and winning_num != "" and winning_num in card_nums:
            if sum == 0 or sum == 1:
                sum += 1
            else:
                sum *= 2

    return sum


def part_two(input_file):
    line_list = input_file.readlines()
    length = len(line_list)

    card_totals = [1] * (length)
    num_of_cards = 0

    for x, line in enumerate(line_list):
        # print("CARD " + str(x + 1))
        start_index = line.find(":") + 2
        line = line[start_index:-1]
        split_line = line.split(" | ")
        winning_nums = split_line[0].split(" ")
        card_nums = split_line[1].split(" ")

        number_of_winning_nums = 0
        # gets number of winning numbers in the card
        for winning_num in winning_nums:
            if winning_num != " " and winning_num != "" and winning_num in card_nums:
                number_of_winning_nums += 1
        # print("NUM OF WINNING NUMS: " + str(number_of_winning_nums))

        if number_of_winning_nums != 0:
            for z in range(number_of_winning_nums):
                card_totals[z + x + 1] += card_totals[x]

        print(card_totals)
        print("\n")

    # calculate number of total scratch cards
    for card_total in card_totals:
        num_of_cards += card_total

    return num_of_cards
