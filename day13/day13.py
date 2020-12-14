import os, string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

earliest_depart = int(lines[0].replace('\n',''))
bus_times = []

#PART 1
def part1():
    for time in lines[1].split(','):
        if time != 'x':
            bus_times.append(int(time))

    bus_earliest_time = {}
    earliest_bus = [0,10000]

    for time in bus_times:        
        print((( 1 - ((earliest_depart / time) % 1)) * time))
        bus_earliest_time[time] = int(earliest_depart + (( 1 - ((earliest_depart / time) % 1)) * time)) - earliest_depart
        if bus_earliest_time[time] < earliest_bus[1]:
            earliest_bus[0] = time
            earliest_bus[1] = bus_earliest_time[time]

    print(earliest_bus[1] * earliest_bus[0])

#PART 2
def part2():
    for time in lines[1].split(','):
        if time != 'x':
            bus_times.append(int(time))
        else:
            bus_times.append(time)
part1()
part2()