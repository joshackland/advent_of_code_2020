import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()


#PART 1
def part1():
    bag_contains = {}
    previous_hold = []
    current_hold = []

    counter = 0

    for line in lines:
        line = line.replace('bags', '').replace('bag','').replace(' ','').replace('\n','')
        bag = line.split('contain')

        if 'noothers' not in bag[1]:
            bag_contains[str(bag[0])] = bag[1]

    for bag, contains in bag_contains.items():
        if 'shinygold' in contains:
            previous_hold.append(bag)
            counter += 1
            
    del bag_contains['shinygold']


    for bag in previous_hold:
        del bag_contains[bag]

    new_bag = True
    while new_bag:    
        new_bag = False
        
        for bag, contains in bag_contains.items(): 
            for prev_bag in previous_hold:
                if prev_bag in contains:
                    current_hold.append(bag)
                    new_bag = True
                    break

        for bag in current_hold:
            if bag in bag_contains:
                del bag_contains[bag]
            previous_hold.append(bag)
        
        counter += len(current_hold)
        current_hold = []
    print(counter)


#PART 2
def bag_count(bag_contains, bag_name):
    bag = bag_contains[bag_name]

    total_counter = 1

    for b, c in bag.items():
        if b == 'noother':
            print(f'{bag_name} 1')
            return total_counter
        else:
            total = bag_count(bag_contains, b) * c        
            total_counter += total
            print(f'{bag_name} {bag} {b} {total} {total_counter}')

    return total_counter

def part2():
    bag_contains = {}

    for line in lines:
        line = line.replace('bags', '').replace('bag','').replace(' ','').replace('\n','').replace('.','')
        bag = line.split('contain')

        contained = {}

        for bags in bag[1].split(','):
            if bags == 'noother':
                contained[bags] = 0
            else:
                contained[bags[1:]] = int(bags[0:1])

            bag_contains[bag[0]] = contained

    print(str(bag_count(bag_contains, 'shinygold') - 1))


part1()
part2()
