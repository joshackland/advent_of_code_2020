import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
Lines = file.readlines()

#PART 1
valid_passwords = 0

for line in Lines:
    l = line.split(' ')
    l[0] = l[0].split('-')
    num1 = int(l[0][0])
    num2 = int(l[0][1])
    l[1] = l[1].replace(':','')
    l[2] = l[2].replace('\\n','')
    
    counter = 0

    for letter in l[2]:
        if l[1] == letter:
            counter += 1

    if counter >= num1 and counter <= num2:
        valid_passwords += 1

print(valid_passwords)


#PART 2
valid_passwords = 0

for line in Lines:
    l = line.split(' ')
    l[0] = l[0].split('-')
    num1 = int(l[0][0])
    num2 = int(l[0][1])
    l[1] = l[1].replace(':','')
    l[2] = l[2].replace('\\n','')

    if l[2][num1-1] == l[1] or l[2][num2-1] == l[1]:
        valid_passwords += 1
        if l[2][num1-1] == l[1] and l[2][num2-1] == l[1]:
            valid_passwords -= 1

print(valid_passwords)