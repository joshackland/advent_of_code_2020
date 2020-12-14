import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

numbers = []
for line in lines:
    numbers.append(int(line.replace('\n','')))

numbers.append(0)
sort_num = sorted(numbers)

#PART 1
def part1():
    counter_1 = 0
    counter_3 = 1
    prev_num = 0

    for num in sort_num:
        if num - prev_num == 1:
            counter_1 += 1
        elif num - prev_num == 3:
            counter_3 += 1

        prev_num = num

    print(f'{counter_1} {counter_3}')
    print(f'{counter_1*counter_3}')

#PART 2
def part2():

    checked = {}

    def check(index, jump):
        if jump < len(sort_num) and sort_num[jump] - sort_num[index] <= 3:
            return True
        return False

    def recursion(index):
        if index == len(sort_num):
            return 1

        if index in checked:
            return checked[index]

        total = 0
        total += recursion(index + 1)

        if check(index, index + 2):
            total += recursion(index + 2)

            if check(index, index + 3):
                total += recursion(index + 3)

        checked[index] = total

        return total
    
    print(recursion(0))

part1()
part2()