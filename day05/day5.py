import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()


#PART 1
boarding_ids = []
highest_id = 0

for line in lines:
    line = line.replace('\n','')

    lower_row = 0
    upper_row = 127
    row = 0
    lower_column = 0
    upper_column = 7
    column = 0

    for letter in line[0:7]: 
        if letter == 'F':
            if upper_row - lower_row == 1:
                row = lower_row
            else:
                upper_row = upper_row - int(((upper_row - lower_row) / 2)) - 1
        else:
            if upper_row - lower_row == 1:
                row = upper_row
            else:
                lower_row = lower_row + int(((upper_row - lower_row) / 2)) + 1
    
    for letter in line[-3:]:
        if letter == 'L':
            if upper_column - lower_column == 1:
                column = lower_column
            else:
                upper_column = upper_column - int(((upper_column - lower_column) / 2)) - 1
        else:
            if upper_column - lower_column == 1:
                column = upper_column
            else:
                lower_column = lower_column + int(((upper_column - lower_column) / 2)) + 1
        
    
    id = (row * 8) + column
    
    if id > highest_id:
        highest_id = id
    
    boarding_ids.append(id)

print(highest_id)

#PART 2
boarding_ids = sorted(boarding_ids)

for i in range(1, len(boarding_ids) - 2):
    c_id = boarding_ids[i]
    if c_id - 1 != boarding_ids[i-1]: 
        print(c_id - 1)
    elif c_id +1 != boarding_ids[i+1]:
        print(c_id + 1)