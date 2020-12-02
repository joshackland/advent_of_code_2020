import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
Lines = file.readlines()

list_of_num = []

for num in Lines:
    list_of_num.append(int(num))

list_of_num = sorted(list_of_num)

#PART 1
found_2020 = False

for i in range(0,len(list_of_num)):
    num1 = list_of_num[i]
    for j in range(i+1,len(list_of_num)):
        num2 = list_of_num[j]
        if num1 + num2 > 2020:
            break
        if num1 + num2 == 2020:
            print(f'num1 = {num1}, num2 = {num2}, sum = {str(num1+num2)} product = {str(num1*num2)}')
            found_2020 = True
            break
    if found_2020:
        break

#PART 2
found_2020 = False

for i in range(0,len(list_of_num)):
    num1 = list_of_num[i]
    for j in range(i+1,len(list_of_num)):
        num2 = list_of_num[j]
        for k in range(j+1,len(list_of_num)):
            num3 = list_of_num[k]
            if num1 + num2 + num3 > 2020:
                break
            if num1 + num2 + num3 == 2020:
                print(f'num1 = {num1}, num2 = {num2}, num3 = {num3}, sum = {str(num1+num2+num3)} product = {str(num1*num2*num3)}')
                found_2020 = True
                break
        if found_2020:
            break
    if found_2020:
        break