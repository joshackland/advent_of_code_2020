import os, string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

#PART1
def part1():
    memory = {}
    mask = ''
    for instruction in lines:
        instruction = instruction.replace('\n','')
        if instruction[0:4] == 'mask':
            mask = instruction.split(' ')[2]
        else:
            mem_location = instruction.split(' ')[0].split('[')[1].replace(']','')
            mem_value = bin(int(instruction.split(' ')[2])).replace('0b','')
            new_mem_value = mask

            for i in range(1, len(mem_value) + 1):
                if new_mem_value[len(new_mem_value) - i] == 'X':
                    #new_mem_value[len(new_mem_value) - i] = mem_value[len(mem_value) - i]
                    new_mem_value = new_mem_value[0:len(new_mem_value) - i] + mem_value[len(mem_value) - i] + new_mem_value[len(new_mem_value) - i + 1:]
            
            new_mem_value = new_mem_value.replace('X','0')
            memory[mem_location] = int(new_mem_value,2)

    total = 0
    for location, value in memory.items():
        total += value
    
    print(total)

def find_addresses(mem_location, indexes, index):
    addresses = []
    new_addresses = []

    mem_location = mem_location[0:indexes[index]-1] + "0" + mem_location[indexes[index]:]

    
    if index + 1 != len(indexes):
        new_addresses.append(find_addresses(mem_location, indexes, index+1))
    else:
        addresses.append(mem_location)

    mem_location = mem_location[0:indexes[index]-1] + "1" + mem_location[indexes[index]:]

    if index + 1 != len(indexes):
        new_addresses.append(find_addresses(mem_location, indexes, index+1))
    else:
        addresses.append(mem_location)

    for a_list in new_addresses:
        for a in a_list:
            addresses.append(a)

    return addresses

#PART2
def part2():
    memory = {}
    mask = ''
    for instruction in lines:
        instruction = instruction.replace('\n','')
        if instruction[0:4] == 'mask':
            mask = instruction.split(' ')[2]
        else:
            mem_location = bin(int(instruction.split(' ')[0].split('[')[1].replace(']',''))).replace('0b','')
            mem_value = int(instruction.split(' ')[2])

            if len(mem_location) < 36:
                mem_location = ('0' * (36 - len(mem_location))) + mem_location

            indexes = []
            for i in range(0,len(mask)):
                if mask[i] == 'X':
                    indexes.append(i+1)
                elif mask[i] == '1':
                    mem_location = mem_location[0:i] + '1' + mem_location[i+1:]

            addresses = find_addresses(mem_location, indexes, 0)

            for a in addresses:
                memory[a] = mem_value

    total = 0
    for location, value in memory.items():
        total += value
    
    print(total)

#part1()
part2()