import os, string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

input = []
for line in lines:
    for n in line.split(','):
        input.append(int(n))

#PART 1
def part1():
    num_previous = {}
    current_num = 0

    for i in range(0, 2020):
        if i < len(input):
            current_num = input[i]
            if i + 1 < len(input):
                num_previous[current_num] = i
        else:
            if current_num not in num_previous:
                num_previous[current_num] = i-1
                current_num = 0
            else:
                previous_turn = num_previous[current_num]
                num_previous[current_num] = i-1
                current_num = i-1 - previous_turn

    print(current_num)
    

#PART 2
def part2():
    num_previous = {}
    current_num = 0

    i = 0

    while True:
        if i < len(input):
            current_num = input[i]
            if i + 1 < len(input):
                num_previous[current_num] = i
        else:
            if current_num not in num_previous:
                num_previous[current_num] = i-1
                current_num = 0
            else:
                previous_turn = num_previous[current_num]
                num_previous[current_num] = i-1
                current_num = i-1 - previous_turn
        
        i += 1
        if i == 30000000:
            break

    print(current_num)

part1()
part2()