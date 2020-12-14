import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

required_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []
passport = {}


for line in lines:
    if line == '\n':        
        passports.append(passport)
        passport = {}
    else:
        line = line.replace('\n', '')
        for no_space in line.split(' '):
            no_colon = no_space.split(':')
            passport[no_colon[0]] = no_colon[1]

if passport != {}:
    passports.append(passport)

valid_counter = 0

for pa in passports:
    counter = 0
    for detail in pa:
        if detail in required_details:
            counter += 1
    
    if counter == len(required_details):
        valid_counter += 1

print(valid_counter)

#PART 2

valid_counter = 0

for pa in passports:
    is_valid = True
    counter = 0
    for detail in pa:
        if detail in required_details:
            counter += 1
    
    if counter < len(required_details):
        is_valid = False
    else:
        if len(pa['byr']) != 4 or not 1920 <= int(pa['byr']) <= 2002:
            is_valid = False
        
        if len(pa['iyr']) != 4 or not 2010 <= int(pa['iyr']) <= 2020:
            is_valid = False
        
        if len(pa['eyr']) != 4 or not 2020 <= int(pa['eyr']) <= 2030:
            is_valid = False

        if not ((pa['hgt'][-2:] == 'in' and 59 <= int(pa['hgt'][:-2]) <= 76) or (pa['hgt'][-2:] == 'cm' and 150 <= int(pa['hgt'][:-2]) <= 193)):
                is_valid = False
        
        if pa['hcl'][0] != '#' or len(pa['hcl']) != 7:
            is_valid = False

        else:
            for hex in pa['hcl'][1:0]:
                if hex not in string.hexdigits:        
                    is_valid = False
        
        if pa['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            is_valid = False
        
        if not (len((pa['pid'])) == 9 and pa['pid'].isnumeric()):
            is_valid = False
    
    if is_valid:
        valid_counter += 1

print(valid_counter)
