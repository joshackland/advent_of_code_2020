import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

numbers = []
for line in lines:
    numbers.append(int(line.replace('\n','')))

#PART 1
def part1():
    for i in range(25, len(numbers) - 1):
        success = False
        for j in range(i-25, i-1):
            for k in range(j+1, i):
                if numbers[j] + numbers[k] == numbers[i]:
                    success = True
                    break
            if success:
                break
        
        if not success:
            print(f'{numbers[i]}')
            break
    return i

def part2(invalid_index):    
    success = False
    min_index = -1

    while not success:
        counter = 0
        min_index += 1
        current_index = min_index
        current_max = 0

        while counter < numbers[invalid_index]:                   
            if min_index != invalid_index:             
                counter += numbers[current_index]
                current_max = numbers[current_index]
            else:
                break
            current_index += 1
        
        if counter == numbers[invalid_index]:
            success = True
            num_list = []

            for i in range(min_index, current_index):
                num_list.append(numbers[i])

            num_list = sorted(num_list)
            print(f'{num_list[0] + num_list[-1]}')



index = part1()
part2(index)