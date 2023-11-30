with open('src/data/task3.txt', 'r') as file3:
    text_lines = file3.readlines()
    for i in range(len(text_lines)):
        if i % 2 == 0:
            print(text_lines[i][:-2])
    for i in range(len(text_lines)):
        if i % 2 == 1:
            print(text_lines[i][:-2])
