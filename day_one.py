def part_one():
    input_file = open("input.txt", "r")
    overall_num = 0
    for line in input_file:
        line_num = ""
        length = len(line)

        first_found = False
        last_found = False
        for character in line:
            if first_found is False:
                if character.isdigit():
                    line_num = character + line_num
                    first_found = True

            if last_found is False:
                rev_chararacter = line[length - 1]
                if rev_chararacter.isdigit():
                    line_num = line_num + rev_chararacter
                    last_found = True
                length = length - 1

            if first_found is True and last_found is True:
                break

        overall_num = overall_num + int(line_num)
    input_file.close()
    return overall_num


def part_two():
    number_strs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    input_file = open("input.txt", "r")
    overall_num = 0

    for line in input_file:
        length = len(line)

        first_found = False
        last_found = False
        first_value = ""
        last_value = ""
        first_index = -1
        last_index = -1

        for index, character in enumerate(line):
            if first_found is False:
                if character.isdigit():
                    first_found = True
                    first_index = index
                    first_value = character

            if last_found is False:
                rev_chararacter = line[length - 1]  # length - index - 1
                if rev_chararacter.isdigit():
                    last_found = True
                    last_index = length - 1
                    last_value = rev_chararacter
                length = length - 1

            if first_found is True and last_found is True:
                break

        for x, num in enumerate(number_strs):  # x is
            index_of_number = line.find(num)
            last_index_of_number = line.rfind(num)
            if index_of_number != -1:
                if index_of_number < first_index:
                    first_value = x
                    first_index = index_of_number
                if index_of_number > last_index:
                    last_value = x
                    last_index = index_of_number

            if last_index_of_number != -1:
                if last_index_of_number < first_index:
                    first_value = x
                    first_index = last_index_of_number
                elif last_index_of_number >= last_index:
                    last_value = x
                    last_index = last_index_of_number

        line_num = str(first_value) + str(last_value)
        overall_num = overall_num + int(line_num)
    input_file.close()
    return overall_num
