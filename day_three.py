def day(input_file):
    part_one(input_file)


def part_one(input_file):
    total_sum = 0

    line_list = input_file.readlines()
    length = len(line_list)

    for x, line in enumerate(line_list):
        total_sum += find_number(line, x, line_list, length)

    return total_sum

def find_number(line, line_num, line_list, length):
    number = ""
    symbol_near = False
    line_sum = 0
    last_char_before_num = ""

    for y, character in enumerate(line):
        # check prior character where???
        if character.isnumeric():
            number += character
        else:
            if y == 0:
                last_char_before_num = line[0]

            if number != "":  # can end collecting number
                if character != "." and character != "\n" or (last_char_before_num != "." and last_char_before_num != ""):
                    symbol_near = True

                if symbol_near is False:
                    if line_num == 1:
                        print("yoooooo " + number)

                    if line_num == 0:
                        symbol_near = check_first_line(number, y, line, line_list[line_num + 1])
                    elif line_num == length - 1:
                        symbol_near = check_last_line(number, y, line, line_list[line_num-1])
                    else:
                        symbol_near = check_symbol_diagonal(number, y, line, line_list[line_num + 1],
                                                            line_list[line_num - 1], line_num, character, last_char_before_num)

                if symbol_near is True:
                    line_sum += int(number)

                    print(character)
                    print("ADDED " + number)
                    #print(line_sum)
                    symbol_near = False
            number = ""
            last_char_before_num = character
    return line_sum



def check_last_line(number, current_index, line, prev_line):
    prev_line_symbols = prev_line[current_index - len(number) - 1:current_index + 1]
    prev_length = len(prev_line_symbols)

    if prev_line_symbols.count(".") != prev_length:
       # print("YES")
        return True
    return False

def check_first_line(number, current_index, line, next_line):

    next_line_symbols = next_line[current_index - len(number) - 1:current_index + 1]
    next_length = len(next_line_symbols)

    if next_line_symbols.count(".") != next_length:
        #print("YES")
        return True

    return False


def check_symbol_diagonal(number, current_index, line, next_line, prev_line, line_number, character, last_char_before_num):
    # edge case: number is first/last in the line

    if last_char_before_num == "":
        prev_line_symbols = prev_line[0:current_index + 1]
        next_line_symbols = next_line[0:current_index + 1]
    else:
        prev_line_symbols = prev_line[current_index - len(number) - 1:current_index + 1]
        next_line_symbols = next_line[current_index - len(number) - 1:current_index + 1]

    prev_length = len(prev_line_symbols)
    next_length = len(next_line_symbols)

    #if line_number == 1:
    #    print(prev_line_symbols)
    #    print(" " + number + " ")
   #     print(next_line_symbols)

    if character == "\n":
        prev_length -= 1
        next_length -= 1

    #if line_number == 11:
       # print(number + " " + prev_line_symbols)
       # print(str(prev_line_symbols.count(".")) + "   " + str(prev_length))

    if prev_line_symbols.count(".") != prev_length:
      #  if line_number == 1:
           # print(number + " YES")
        return True

    if next_line_symbols.count(".") != next_length:
       # if line_number == 1:
           # print(number + " YES")
        return True

    return False


# 470062
# 475156 too low
# 513576
# 512645
# 516986


#to try:
#    514969