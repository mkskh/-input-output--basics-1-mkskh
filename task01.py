# with open(file='src/data/task1.txt', mode='r') as file1:
#     content = file1.read()
#     print(content)

# try:
#     file1.readable()
# except ValueError:
#     print('The file is closed')


file1 = open('src/data/task1.txt', 'r')
# print(file1)
content = file1.read()
print(content)
# print(file1.readable())
file1.close()


try:
    file1.readable()
except ValueError:
    print('---The file is closed---')