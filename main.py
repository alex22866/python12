# file = open('text.txt', 'a')
# file.write('world')
#
#
# if __name__ == '__main__':
#     pass


# import csv
# d = {    }
#
# with open('db.csv.csv', encoding='utf8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
#
# if __name__ == '__main__':
#     pass

#file = open(r'C:\Users\Alexandra\PycharmProjects\python12\text.txt', 'r')
#print(file.readline())                 #file.readline - читает всю строку, Пишет по счету букву
# print(file.read(1))                   #file.read - читает строку по букве, Пишет по счету букву


# for i in file:    #читает все строки
#     for e in i:
#      print(e)
#
#
# if __name__ == '__main__':
#     pass

# file = open ('text.txt', 'r')
# for row in file:                            #цикл по букве в строке
#     for letter in row:
#      print(letter)

file = open ('text.txt')
s = file.readlines()
print(s)
