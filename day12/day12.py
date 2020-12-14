import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

instructions = []
for line in lines:
    instructions.append(line.replace('\n',''))

#PART 1
def move(axis, direction, distance):
    if direction == 0:
        axis['y'] += distance
    elif direction == 90:
        axis['x'] += distance
    elif direction == 180:
        axis['y'] -= distance
    elif direction == 270:
        axis['x'] -= distance

def part1():
    previous_direction = 90
    axis = {}
    axis['x'] = 0
    axis['y'] = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'N':
            move(axis, 0, distance)
        elif direction == 'S':
            move(axis, 180, distance)
        elif direction == 'E':
            move(axis, 90, distance)
        elif direction == 'W':
            move(axis, 270, distance)
        elif direction == 'L':
            previous_direction = (previous_direction - distance) % 360
        elif direction == 'R':
            previous_direction = (previous_direction + distance) % 360

        elif direction == 'F':
            move(axis, previous_direction, distance)
            

    if axis['x'] < 0:
        axis['x'] *= -1

    if axis['y'] < 0:
        axis['y'] *= -1

    print(axis['x'] + axis['y'])


#PART 2
def change_units(units, direction, distance):
    if ((units['l'][0] - direction) / 90) % 2 == 0:
        if units['l'][0] == direction:
            units['l'][1] += distance
        else:
            units['l'][1] -= distance
    elif ((units['r'][0] - direction) / 90) % 2 == 0:
        if units['r'][0] == direction:
            units['r'][1] += distance
        else:
            units['r'][1] -= distance

def move_units(axis, units, distance):
    if units['l'][0] == 0:
        axis['y'] += units['l'][1] * distance
        axis['x'] += units['r'][1] * distance
    if units['l'][0] == 90:
        axis['y'] -= units['r'][1] * distance
        axis['x'] += units['l'][1] * distance
    if units['l'][0] == 180:
        axis['y'] -= units['l'][1] * distance
        axis['x'] -= units['r'][1] * distance
    if units['l'][0] == 270:
        axis['y'] += units['r'][1] * distance
        axis['x'] -= units['l'][1] * distance

def part2():
    units = {}
    units['l'] = [0, 1]
    units['r'] = [90, 10]

    axis = {}
    axis['x'] = 0
    axis['y'] = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'N':
            change_units(units, 0, distance)
        elif direction == 'S':
            change_units(units, 180, distance)
        elif direction == 'E':
            change_units(units, 90, distance)
        elif direction == 'W':
            change_units(units, 270, distance)
        elif direction == 'L':
            units['l'][0] = (units['l'][0] - distance) % 360
            units['r'][0] = (units['r'][0] - distance) % 360
        elif direction == 'R':
            units['l'][0] = (units['l'][0] + distance) % 360
            units['r'][0] = (units['r'][0] + distance) % 360

        elif direction == 'F':
            move_units(axis, units, distance)

    if axis['x'] < 0:
        axis['x'] *= -1

    if axis['y'] < 0:
        axis['y'] *= -1

    print(axis['x'] + axis['y'])

part1()
part2()