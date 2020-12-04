import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def split(row):
    return [char for char in row]

file = open(dir_path + '/' + 'file.txt', 'r')
Lines = file.readlines()

passports = []
passport = ''
for line in Lines:
    if line != '\n':
        passport += line.replace('\n','')
        passport += ' '
    else:
        passports.append(passport)
        passport = ''

#PART 1
passport_details = {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False}

passport_counter = 0

for passport in passports:
    details = passport.split(' ')
    valid_counter = 0
    for key_value in details:
        kv = key_value.split(':')
        passport_details[kv[0]] = True

    for pd in passport_details.items():
        if pd[1] == True:
            valid_counter += 1

    if valid_counter >= len(passport_details.items()):
        print(passport)
        passport_counter += 1
        
print (passport_counter)



#PART 2