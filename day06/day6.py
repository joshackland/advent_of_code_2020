import os, string
dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + '/' + 'file.txt', 'r')
lines = file.readlines()

#PART 1
questions = {}
total = 0

for line in lines:
    if line == '\n':
        total += len(questions)
        questions = {}
    else:
        line = line.replace('\n','')
        for letter in line:        
            questions[letter] = 1

total += len(questions)

print(total)


#PART 2
questions = {}
total = 0
counter = 0

for line in lines:
    if line == '\n':
        for question in questions.items():
            if question[1] == counter:
                total += 1
        questions = {}
        counter = 0
    else:
        counter += 1
        line = line.replace('\n','')
        for letter in line:        
            if letter not in questions:
                questions[letter] = 1
            else:
                questions[letter] += 1

for question in questions.items():
    if question[1] == counter:
        total += 1

print(total)