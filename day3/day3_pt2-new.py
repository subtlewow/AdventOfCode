import re
from functools import reduce

pattern = r'\*'
num_pattern = r'[0-9]'
grid = []
number = ""

adjacent_icon_indices = {}
adjacency_lst = []

final = 0
product = 1

def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def is_adjacent(row, col, char_array, pattern_type=pattern):
    max_row = len(char_array)
    max_col = len(char_array[0]) if max_row > 0 else 0
    indices = []
    
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
    
    for direction, (row, col) in directions.items():
        
        # matches both gear icons '*' and numbers
        if is_valid_position(row, col, max_row, max_col):
            match = re.match(pattern_type, char_array[row][col])
            
            if match:
                if char_array[row][col] == '*':
                    return [row, col]
                else:
                    indices.append([row, col])
            
    return indices
            
with open('./inputs/day3.txt', 'r') as f:
    
    first = False
    last = False
    
    first_idx = -1
    last_idx = -1
    
    # parse input into 2D grid format for easier processing
    for line in f:
        line = line.strip('\n')
        grid.append(list(line))
    
    for row, line in enumerate(grid):
        number = ""
        adjacency_lst = []
        product = 1
        first = False
        last = False    
        first_idx = -1
        last_idx = -1

        for col, _ in enumerate(line):
            char = line[col]
            # generating number, and enumerating first / last indices for given number
            if char.isdigit():
                if is_adjacent(row, col, grid):
                    adjacency_lst.append(is_adjacent(row, col, grid))
                
                # checking first occurrence
                if not number and not first:
                    first = True
                    first_idx = col
                    
                number += char
                
                # adjacency will be indices of type list where adjacency occurs
                
                # checking last occurrence
                if not last and col+1 < len(line) and not line[col+1].isdigit():
                    last = True
                    last_idx = col
                elif col+1 == len(line):
                    last = True
                    last_idx = col
                
                # append to dict only when number is created and final index is found
                if first and last:
                    first = False
                    last = False

                    if adjacency_lst:
                        ridx, cidx = adjacency_lst[0]
                        
                        # adj_arr returns index of gear icon occurrences
                        adj_arr = is_adjacent(ridx, cidx, grid, num_pattern)
                        combinations = [[row, num] for num in range(first_idx, last_idx+1)]
                        
                        # if true, digit is adjacent to gear icon
                        if adj_arr:
                            adj_str = "".join(map(str, adjacency_lst[0]))
                            # check if gear icon index is identical to any adjacent digits
                            if any(lst in combinations for lst in adj_arr):
                                # map the number for that gear icon
                                if adj_str not in adjacent_icon_indices:
                                    adjacent_icon_indices[adj_str] = [int(number)]
                                else:
                                    adjacent_icon_indices[adj_str].append(int(number))
                                    
            else:   
                number = ""
                adjacency_lst = []
                product = 1
                first = False
                last = False    
                first_idx = -1
                last_idx = -1
                
    print(adjacent_icon_indices)

    # multiply numbers then sum up
    for values in adjacent_icon_indices.values():
        if len(values) == 2:        
            final += (values[0] * values[1])
            
        # print(final)
        
    print(final)
            
            # check if character is gear symbol, then check adjacency
            # if char == '*':
            #     is_adjacent(row, col, grid)
            
            
            
            
        
