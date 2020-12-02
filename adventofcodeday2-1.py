passwords = open("C:\\users\\WORKSPACE\\desktop\\passwords.txt", "r")
password_list = []

for line in passwords:
    new_line = line.strip()
    new_line = new_line.split(":")
    password_list.append(new_line)


conts = []
password = []

for i in range(len(password_list)):
    conts.append(password_list[i][0])
    password.append(password_list[i][1].strip(' '))


valid = 0

for i in range(len(password)):

    y = (conts[i].split(' '))
    nums = (y[0].split('-'))
    n = (password[i].count(y[1]))
    if n >= int(nums[0]) and n <= int(nums[1]):
        valid += 1

print ("there are {} valid passwords".format(valid))