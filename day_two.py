def day(input_file):
    return part_two(input_file)

def part_one(input_file):
    possible_games_sum = 0

    # get each game
    for game_num, line in enumerate(input_file):
        is_possible = True

        # parse to colon
        start_index = line.find(":") + 2
        line = line[start_index:-1]

        red_limit = 12
        green_limit = 13
        blue_limit = 14

        # get each set
        sets = line.split("; ")
        for block_set in sets:
            blocks = block_set.split(", ")
            #print("block_set " + block_set)

            for block in blocks:
                num_index = block.find(" ")
                num = block[:num_index]
                color = block[num_index+1:]
                #print("block " + block)

                if color == "red" and int(num) > red_limit:
                    print("FALSE " + num + " red")
                    is_possible = False
                elif color == "green" and int(num) > green_limit:
                    print("FALSE " + num + " green")
                    is_possible = False
                elif color == "blue" and int(num) > blue_limit:
                    print("FALSE " + num + " blue")
                    is_possible = False

            if is_possible is False:
                break

        if is_possible is True:
            possible_games_sum = possible_games_sum + game_num + 1

    return possible_games_sum


def part_two(input_file):
    total_power = 0

    # get each game
    for game_num, line in enumerate(input_file):
        # parse to colon
        start_index = line.find(":") + 2
        line = line[start_index:-1]

        red_min = 0
        blue_min = 0
        green_min = 0

        # get each set
        sets = line.split("; ")
        for block_set in sets:
            blocks = block_set.split(", ")

            for block in blocks:
                num_index = block.find(" ")
                num = block[:num_index]
                color = block[num_index + 1:]

                if color == "red" and int(num) > red_min:
                    red_min = int(num)
                elif color == "green" and int(num) > green_min:
                    green_min = int(num)
                elif color == "blue" and int(num) > blue_min:
                    blue_min = int(num)

        total_power += (red_min * green_min * blue_min)

    return total_power
