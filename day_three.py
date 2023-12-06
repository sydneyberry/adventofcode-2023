def part_two(input_file):
    total_sum = 0

    line_list = input_file.readlines()
    length = len(line_list)

    for x, line in enumerate(line_list):
        find_numbers_in_line_pt2(line, x, line_list, length)

    return 0

def find_numbers_in_line_pt2(line, line_num, line_list, length):
    index = 0

    while index != -1:
        first_num = ""
        last_num = ""
        index = line.find("*", index + 1)

        #print(index)
        if line_num != 0 and line_num != length-1:      # add edge cases
            next_line = line_list[line_num + 1]
            prev_line = line_list[line_num - 1]

            if first_num == "" and last_num == "":
                #if prev_line[index-1:index+1]



                if line[index-1].isnumeric():
                    get_full_number(line, index-1)

                if line[index+1].isnumeric():
                    get_full_number(line, index+1)



        # check index 0 and end of line


def get_full_number(line, index):
   # if index != 0 and line[index] != "\n":
    return 0











def part_one(input_file):
    total_sum = 0

    line_list = input_file.readlines()
    length = len(line_list)

    for x, line in enumerate(line_list):
        total_sum += find_numbers_in_line_pt1(line, x, line_list, length)

    return total_sum

def find_numbers_in_line_pt1(line, line_num, line_list, length):
    number = ""
    symbol_near = False
    line_sum = 0
    last_char_before_num = ""

    for y, character in enumerate(line):
        if character.isnumeric():
            number += character
        else:
            if y == 0:
                last_char_before_num = line[0]

            if number != "":  # can end collecting number
                if character != "." and character != "\n" or (last_char_before_num != "." and last_char_before_num != ""):
                    symbol_near = True

                if symbol_near is False:
                    if line_num == 0:
                        symbol_near = check_first_line_diagonal(number, y, line, line_list[line_num + 1])
                    elif line_num == length - 1:
                        symbol_near = check_last_line_diagonal(number, y, line, line_list[line_num-1])
                    else:
                        symbol_near = check_symbol_diagonal(number, y, line, line_list[line_num + 1],
                                                            line_list[line_num - 1], line_num, character, last_char_before_num)

                if symbol_near is True:
                    line_sum += int(number)
                    symbol_near = False
            number = ""
            last_char_before_num = character
    return line_sum



def check_last_line_diagonal(number, current_index, line, prev_line):
    prev_line_symbols = prev_line[current_index - len(number) - 1:current_index + 1]
    prev_length = len(prev_line_symbols)

    if prev_line_symbols.count(".") != prev_length:
        return True
    return False

def check_first_line_diagonal(number, current_index, line, next_line):

    next_line_symbols = next_line[current_index - len(number) - 1:current_index + 1]
    next_length = len(next_line_symbols)

    if next_line_symbols.count(".") != next_length:
        return True

    return False


def check_symbol_diagonal(number, current_index, line, next_line, prev_line, line_number, character, last_char_before_num):
    if last_char_before_num == "":
        prev_line_symbols = prev_line[0:current_index + 1]
        next_line_symbols = next_line[0:current_index + 1]
    else:
        prev_line_symbols = prev_line[current_index - len(number) - 1:current_index + 1]
        next_line_symbols = next_line[current_index - len(number) - 1:current_index + 1]

    prev_length = len(prev_line_symbols)
    next_length = len(next_line_symbols)

    if character == "\n":
        prev_length -= 1
        next_length -= 1

    if prev_line_symbols.count(".") != prev_length:
        return True

    if next_line_symbols.count(".") != next_length:
        return True

    return False
