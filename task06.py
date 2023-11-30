with open('src/data/task6.txt','r') as file:
    lines_list = file.readlines()
    every_line_length = []

    for position in lines_list:
        count_letters_in_position = 0
        for letter in position:
            count_letters_in_position += 1
        every_line_length.append(count_letters_in_position)

print(every_line_length)