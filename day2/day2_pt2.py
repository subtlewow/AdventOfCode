total_power_cubes = 0

with open('./day2/day2.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')

        game_id = int(line.split(':')[0].split(' ')[1])
        elements = line.split(':')[1].strip(' ').split(' ')
        
        element_count = {'red': 0, 'green': 0, 'blue': 0}
        power_of_cubes = 1

        j = 0
        while j < len(elements):
            char = ',' if ',' in elements[j+1] else ';'
            key = elements[j+1].strip(char)
            value = int(elements[j])
            element_count[key] = max(element_count[key], value)
            j += 2
        
        for count in element_count.values():
            power_of_cubes *= count
        
        total_power_cubes += power_of_cubes
    
    # correct answer: 72513
    print(total_power_cubes)