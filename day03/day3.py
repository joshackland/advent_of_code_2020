import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def split(row):
    return [char for char in row]

file = open(dir_path + '/' + 'file.txt', 'r')
Lines = file.readlines()

map = []
for l in range(1,len(Lines)):
    map.append(split(Lines[l].replace('\n','')))

#PART 1
tree_counter = 0
right = 0
right_length = len(map[0])

for row in map:
    right = (right + 3) % right_length
    if row[right] == '#':
        tree_counter += 1
        

print (tree_counter)

#PART 2
directions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree_list = []
row_length = len(map[0])

for direction in directions:
    tree_counter = 0
    right = direction[0]
    down = direction[1] - 1
    
    while down < len(map):
        if map[down][right] == '#':
            tree_counter +=1

        right = (right + direction[0]) % row_length
        down += direction[1]
    tree_list.append(tree_counter)

tree_product = 0
for tree in tree_list:
    if tree_product == 0:
        tree_product = tree
    else:
        tree_product *= tree
print(tree_product)

