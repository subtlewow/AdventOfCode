from collections import defaultdict


def parse_input_file(filename: str):
    with open(filename, 'r') as f:
        return [line.strip('\n').strip(' ').split(':')[1].strip(' ').split('|') for line in f]

tickets = parse_input_file('./inputs/day4.txt')
total = 0
items = len(tickets)
new = defaultdict(int)

j = 0
for i in range(items):
    add_total = False
    j = i + 1
    new[j] += 1
    
    unique1 = set()
    unique2 = set()
    
    first, second = tickets[i]

    first = first.split(' ')
    second = second.split(' ')
    
    for num in first:
        if num.isdigit():
            unique1.add(num)
    
    for num in second:
        if num.isdigit():
            unique2.add(num)

    intersection = unique1 & unique2

    total = len(intersection)
    
    if new[j] > 1:
        add_total = True
        add = new[j]
    
    if j > 1:
        end_condition = total + j
    else:
        end_condition = total + 1
    
    # initialise
    while total > 0 and j < end_condition:
        j += 1
        
        if add_total:
            new[j] += add
        else:
            new[j] += 1
    

# correct answer: 5422730
print(sum(new.values()))
