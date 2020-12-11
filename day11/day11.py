import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

layout = []
for line in lines:
    layout.append(list(line.replace('\n','')))

directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

#PART 1
def part1 (layout):
    current_layout = []
    prev_layout = []

    for y in range(0,len(layout)):
        c_row = []
        p_row = []
        for x in range(0,len(layout[0])):
            c_row.append(layout[y][x])
            p_row.append(layout[y][x])
        current_layout.append(c_row)
        prev_layout.append(p_row)

    while True:
        for x in range(0,len(prev_layout[0])):
            for y in range(0,len(prev_layout)):
                if prev_layout[y][x] == 'L':
                    seat_available = True
                    
                    for direction in directions:
                        x_axis = x + direction[0]
                        y_axis = y + direction[1]

                        if x_axis >= 0 and x_axis < len(prev_layout[0]) and y_axis >= 0 and y_axis < len(prev_layout):
                            if prev_layout[y_axis][x_axis] == '#':
                                seat_available = False
                        
                        if not seat_available:
                            break

                    if seat_available:
                        current_layout[y][x] = '#'
                elif prev_layout[y][x] == '#':
                    seat_ocupied = 0

                    for direction in directions:
                        x_axis = x + direction[0]
                        y_axis = y + direction[1]

                        if x_axis >= 0 and x_axis < len(prev_layout[0]) and y_axis >= 0 and y_axis < len(prev_layout):
                            if prev_layout[y_axis][x_axis] == '#':
                                seat_ocupied += 1
                        
                        if seat_ocupied >= 4:
                            break         

                    if seat_ocupied >= 4:
                        current_layout[y][x] = 'L'

        if current_layout == prev_layout:
            break
        
        prev_layout = []
        for y in range(0,len(current_layout)):
            row = []
            for x in range(0,len(current_layout[0])):
                row.append(current_layout[y][x])
            prev_layout.append(row)
    
    counter = 0
    for y in range(0,len(current_layout)):
        for x in range(0,len(current_layout[0])):     
            if current_layout[y][x] == '#':
                counter += 1
    
    print(counter)
    

def part2 (layout):
    current_layout = []
    prev_layout = []

    for y in range(0,len(layout)):
        c_row = []
        p_row = []
        for x in range(0,len(layout[0])):
            c_row.append(layout[y][x])
            p_row.append(layout[y][x])
        current_layout.append(c_row)
        prev_layout.append(p_row)

    while True:
        for x in range(0,len(prev_layout[0])):
            for y in range(0,len(prev_layout)):
                if prev_layout[y][x] == 'L':
                    seat_available = True

                    for direction in directions:
                        x_axis = x + direction[0]
                        y_axis = y + direction[1]

                        while x_axis >= 0 and x_axis < len(prev_layout[0]) and y_axis >= 0 and y_axis < len(prev_layout):
                            if prev_layout[y_axis][x_axis] == '#':
                                seat_available = False
                                break
                            elif prev_layout[y_axis][x_axis] == 'L':
                                break
                            x_axis += direction[0]
                            y_axis += direction[1]

                        if not seat_available:
                            break

                    if seat_available:
                        current_layout[y][x] = '#'
                elif prev_layout[y][x] == '#':
                    seat_ocupied = 0

                    for direction in directions:
                        x_axis = x + direction[0]
                        y_axis = y + direction[1]

                        while x_axis >= 0 and x_axis < len(prev_layout[0]) and y_axis >= 0 and y_axis < len(prev_layout):
                            if prev_layout[y_axis][x_axis] == '#':
                                seat_ocupied += 1
                                break
                            elif prev_layout[y_axis][x_axis] == 'L':
                                break
                            x_axis += direction[0]
                            y_axis += direction[1]

                        if seat_ocupied >= 5:
                            break
          

                    if seat_ocupied >= 5:
                        current_layout[y][x] = 'L'

        if current_layout == prev_layout:
            break
        
        prev_layout = []
        for y in range(0,len(current_layout)):
            row = []
            for x in range(0,len(current_layout[0])):
                row.append(current_layout[y][x])
            prev_layout.append(row)

    counter = 0
    for y in range(0,len(current_layout)):
        for x in range(0,len(current_layout[0])):     
            if current_layout[y][x] == '#':
                counter += 1
    
    print(counter)

part1(layout)
part2(layout)