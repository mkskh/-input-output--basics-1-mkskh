with open('src/data/task2.txt', 'r') as file2:
    todo_list = file2.readlines()
    del todo_list[:2]
    print(len(todo_list))