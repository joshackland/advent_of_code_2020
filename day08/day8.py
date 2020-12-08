import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

#PART 1
def part1():
    accumulator = 0
    indexes=[]

    index = 0

    while index < len(lines):
        line = lines[index].replace('\n','')
        line = line.split(' ')

        if index in indexes:
            break

        indexes.append(index)

        if line[0] == 'acc':
            if line[1][0:1] == '+':
                accumulator += int(line[1][1:])
            else:
                accumulator -= int(line[1][1:])

            index += 1
        elif line[0] == 'jmp':
            if line[1][0:1] == '+':
                index += int(line[1][1:])
            else:
                index -= int(line[1][1:])
                jmp_index = index          
        else:
            index += 1


    print(accumulator)

#PART 2
def part2(jmp_indexes = []):
    accumulator = 0
    indexes=[]

    index = 0
    jmp = -1
    success = True

    while index < len(lines):
        line = lines[index].replace('\n','')
        line = line.split(' ')

        if index in indexes:
            success = False
            jmp_indexes.append(jmp)
            break

        indexes.append(index)

        if line[0] == 'acc':
            if line[1][0:1] == '+':
                accumulator += int(line[1][1:])
            else:
                accumulator -= int(line[1][1:])

            index += 1
        elif line[0] == 'jmp':
            if index in jmp_indexes or jmp != -1:
                if line[1][0:1] == '+':
                    index += int(line[1][1:])
                else:
                    index -= int(line[1][1:])       
            else:
                jmp = index 
                index += 1
        else:
            index += 1

    if success:
        print(accumulator)
        return
    else:
        part2(jmp_indexes)

part1()
part2()