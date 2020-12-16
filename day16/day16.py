import os, string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

valid = []
my_ticket = []
nearby_tickets = []

input_c = 0
for line in lines:
    info = []
    if line != '\n':
        line = line.replace('\n','')
        if input_c == 0:
            for l in line.split(':'):
                if '-' not in l:
                    info.append(l)
                else:
                    l = l.replace(' ','')
                    for n in l.split('or'):
                        v_range = []
                        for n in n.split('-'):
                            v_range.append(int(n))
                        info.append(v_range)
            valid.append(info)
        elif input_c == 1:
            if ':' not in line:
                for l in line.split(','):                    
                    my_ticket.append(int(l))
        elif input_c == 2:
            if ':' not in line:
                for l in line.split(','):                    
                    info.append(int(l))
                nearby_tickets.append(info)
    else:
        input_c += 1

#PART 1
def part1():
    error_rate = 0
    
    invalid_tickets = []
    
    for ticket in nearby_tickets:
        for t in ticket:
            is_valid = False
            for v in valid:
                if v[1][0] <= t <= v[1][1] or v[2][0] <= t <= v[2][1]:
                    is_valid = True
                    break
            if not is_valid:
                error_rate += t
                invalid_tickets.append(ticket)
    
    print(error_rate)

    valid_tickets = [i for i in nearby_tickets if i not in invalid_tickets]
    return valid_tickets

#PART 2
def part2(valid_tickets):
    field_order = {}
    while len(field_order) < len(valid):
        for j in range(0, len(valid_tickets[0])):
            field_order[j] = []
            for i in range(0, len(valid)):
                category_found = True
                if valid[i][0] not in field_order.values():
                    for t in valid_tickets:
                        if not valid[i][1][0] <= t[j] <= valid[i][1][1] and not valid[i][2][0] <= t[j] <= valid[i][2][1]:
                            category_found = False
                            break
                    if category_found:
                        #field_order[j] = valid[i][0]
                        #break
                        field_order[j].append(valid[i][0])
    
    while True:
        no_multiples = True

        for i in range(0, len(field_order)):
            if len(field_order[i]) == 1:
                for k in range(0, len(field_order)):
                    if field_order[i][0] in field_order[k] and i != k and len(field_order[k]) > 1:
                        field_order[k].remove(field_order[i][0])
            else:
                no_multiples = False
        

        if no_multiples:
            break

    output = 1
    for i in range(0, len(field_order)):
        if 'departure' in field_order[i][0]:
            output *= my_ticket[i]
    
    print(output)
                

                

valid_tickets = part1()
part2(valid_tickets)