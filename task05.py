with open('src/data/task5.txt','r') as file:
    lines_list = file.readlines()
    print(lines_list[0])
    count = 0
    for letter in lines_list[0]:
        if letter != '\n':
            count += 1
    print(count)