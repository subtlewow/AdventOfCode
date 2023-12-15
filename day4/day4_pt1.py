
def parse_input_file(filename: str):
    with open(filename, 'r') as f:
        return [line.strip('\n').strip(' ').split(':')[1].strip(' ').split('|') for line in f]

tickets = parse_input_file('./inputs/day4.txt')
total = 0

for ticket in tickets:
    unique1 = set()
    unique2 = set()
    
    first, second = ticket
    
    first = first.split(' ')
    second = second.split(' ')
    
    for num in first:
        if num.isdigit():
            unique1.add(num)
    
    for num in second:
        if num.isdigit():
            unique2.add(num)

    intersection = unique1 & unique2
   
    if len(intersection) > 0:
        total += 2 ** (len(intersection)-1)
    
print(total)

