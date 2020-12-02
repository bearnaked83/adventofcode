passwords = open("C:\\users\\WORKSPACE\\desktop\\input.txt", "r")
password_list = []

for line in passwords:
    new_line = line.strip()
    new_line = new_line.split(":")
    password_list.append(new_line)


conts = []
password = []

for i in range(len(password_list)):
    conts.append(password_list[i][0])
    password.append("x" + password_list[i][1].strip(' '))


valid = 0

for i in range(len(password)):

    y = (conts[i].split(' '))
    nums = (y[0].split('-'))
    pos_1 = int(nums[0])
    pos_2 = int(nums[1])
    
    if password[i][pos_1] == y[1]:
        if password[i][pos_2] != y[1]:
            valid = valid + 1
        
    elif password[i][pos_2] == y[1]:
        valid = valid + 1


    
print ("there are {} valid passwords".format(valid))