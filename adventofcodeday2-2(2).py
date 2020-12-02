with open("C:\\users\\WORKSPACE\\desktop\\input.txt", 'r') as file:
    password_list = [line.split() for line in file.readlines()]
valid = 0
for i in password_list:
    password = (i[2])
    letter = i[1].strip(':')
    index_1 = (i[0].split('-'))[0]
    index_2 = (i[0].split('-'))[1]
    index_1 = int(index_1)
    index_2 = int(index_2)

    if password[index_1 - 1] == letter:
        if password[index_2 - 1 ] != letter:
            valid += 1
    elif password[index_2 - 1] == letter:
        valid += 1

print ("there are {} valid passwords".format(valid))