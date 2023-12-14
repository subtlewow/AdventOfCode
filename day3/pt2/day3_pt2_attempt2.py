import re

pattern = r'\*'
num_pattern = r'[0-9]'
grid = []


def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def is_adjacent(row, col, char_array, pattern_type=pattern):
    '''
    Searching around gear symbol icons for adjacent numbers
    '''
    max_row = len(char_array)
    max_col = len(char_array[0]) if max_row > 0 else 0
    indices = []
    gear_indices = []
    
    directions = {
        "UP": (row-1, col),
        "DOWN": (row+1, col),
        "LEFT": (row, col-1),
        "RIGHT": (row, col+1),
        "UL": (row-1, col-1),
        "UR": (row-1, col+1),
        "LL": (row+1, col-1),
        "LR": (row+1, col+1)
    }
    
    for _, (row, col) in directions.items():
        
        # matches both gear icons '*' and numbers
        if is_valid_position(row, col, max_row, max_col):
            char = char_array[row][col]
            match = re.match(pattern_type, char)
            
            if match:
                if char == '*':
                    gear_indices.append([row, col])
                
                if pattern_type == num_pattern:
                    indices.append([row, col])
                
    return gear_indices, indices
        
def parse_grid_from_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            grid.append(list(line))
            
    return grid

def construct_number(row, col, grid):
    num = 0
    if row < R and col < C and grid[row][col].isdigit():
        num = num * 10 + int(grid[row][col])
        
        
        
        

def main(grid):
    not_in_combinations = []
    number = ""
    adjacent_icon_indices = {}
    adjacency_lst = []

    final = 0
    product = 1
    adj_number = ""
    count_gears = {}
    seen = set()
    count = 0

    first = False
    last = False
    first_idx = -1
    last_idx = -1
    
    for row, line in enumerate(grid):
        number = ""
        first = False
        last = False    
        first_idx = -1
        last_idx = -1

        for col, _ in enumerate(line):
            char = line[col]
            
            if char.isdigit():
                gear_indices, _ = is_adjacent(row, col, grid) # finds indices of gear icons
                if gear_indices:
                    for gear_index in gear_indices:
                        gear_indices_tuple = tuple(gear_index)
                        
                        if gear_indices_tuple not in seen:
                            adjacency_lst.append(gear_indices)
                            seen.add(gear_indices_tuple)
                            count += 1
                
                # constructing number
                if not number and not first:
                    first = True
                    first_idx = col
                    
                number += char
                
                # checking last occurrence
                if not last and col+1 < len(line) and not line[col+1].isdigit():
                    last = True
                    last_idx = col
                elif col == len(line)-1:
                    last = True
                    last_idx = col
                
                # append to dict only when number is created and final index is found
                if first and last:
                    first = False
                    last = False

                    for gear_idx in adjacency_lst:
                        # latest_gear = adjacency_lst[-1]
                        # ridx, cidx = latest_gear[0]
                        ridx, cidx = gear_idx[0]
                        
                        # finds indices of adjacent number digits
                        _, adj_arr = is_adjacent(ridx, cidx, grid, num_pattern)
                        
                        combinations = [[row, num] for num in range(first_idx, last_idx+1)]
                        
                        # if true, digit is adjacent to gear icon
                        if adj_arr:
                            adj_str = "".join(map(str, gear_idx[0]))
                            
                            # check if gear icon index is identical to any adjacent digits
                            # not_in_combinations = [lst for lst in adj_arr if lst not in combinations]
                            
                            if any(lst in combinations for lst in adj_arr):
                                # map the number for that gear icon
                                if adj_str not in adjacent_icon_indices:
                                    adjacent_icon_indices[adj_str] = [int(number)]
                                    count_gears[adj_str] = count
                                else:
                                    adjacent_icon_indices[adj_str].append(int(number))

                        # adjacency_lst = []
                       
            else:   
                number = ""
                first = False
                last = False
                first_idx = -1
                last_idx = -1
                count = 0
                adj_arr = []
                
    print(adjacent_icon_indices)
    print(count_gears)

    # multiply numbers then sum up
    for key, values in adjacent_icon_indices.items():
        if len(values) == 2:        
            final += (values[0] * values[1]) * count_gears[key]
        
        print(final)
    
    return final

filename = './inputs/day3-2.txt'
grid = parse_grid_from_file(filename)
main(grid)