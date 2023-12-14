import re
from functools import reduce

pattern = r'\*' # only look for special chars, excluding '.' chars
num_pattern = r'\d+' # looks for numbers

grid = ""
num = ""
asterik = '*'
found = False


def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def is_adjacent_number(row, col, char_array):
    max_row = len(char_array)
    max_col = len(char_array[0]) if max_row > 0 else 0
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
        if is_valid_position(row, col, max_row, max_col):
            match = re.match(pattern, char_array[row][col])
            if match:
                return [row, col]
    
    return False

def is_adjacent_asteriks(row, col, char_array):
    max_row = len(char_array)
    max_col = len(char_array[0]) if max_row > 0 else 0
    idx_array = []
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
        if is_valid_position(row, col, max_row, max_col):
            match = re.match(num_pattern, char_array[row][col])
            if match:
                idx_array.append([row, col])
    
    return idx_array if len(idx_array) > 0 else []


def construct_grid_numbers(char_array, num=""): 
    first = False 
    last = False 
    adjacent = False
    asteriks = False
    
    first_idx = -1
    last_idx = -1 
    
    idx_array = []
    number = []
    final = 1
    final_count = 0
    
    num_idx_map = {}
    
    for row, line in enumerate(char_array):
        first_idx, last_idx = -1, -1
        adjacent = False
        first = False
        last = False
        num = ""
        for col, _ in enumerate(line):
            current_char = line[col]
            
            if current_char.isdigit():
                if not num and not last:
                    first = True
                    first_idx = col
                    
                num += current_char
                
                if is_adjacent_number(row, col, char_array):
                    adjacent = True
                
                if col+1 < len(line) and not line[col+1].isdigit():
                    last = True
                    last_idx = col
            else:
                if current_char == asterik:
                    idx_array = is_adjacent_asteriks(row, col, char_array) # tracks the position of asteriks, will use to check adjacent elements to this position to determine numbers
                
                if idx_array and len(idx_array) <= 2:
                    idx_array = []
                    num_idx_map = {}
                    break
                
                first_idx, last_idx = -1, -1
                adjacent = False
                first = False
                last = False
                num = ""
            
            if first and last and adjacent:
                num_idx_map[int(num)] = [row, [first_idx, last_idx]]
                
        
        if idx_array and len(idx_array) >= 2 and len(num_idx_map) > 1:
            items = list(num_idx_map.items())
            
            for i, item in enumerate(items):
                key, curr_vals = item
                
                for x in range(curr_vals[1][0], curr_vals[1][1]+1):
                    combination = [curr_vals[0], x]
                        
                    if combination in idx_array:
                        number.append(key)
                    
                    if len(number) == 2:
                        final = reduce(lambda x, y: x * y, number)
                        final_count += final
                        final = 1
                        number = []
                        num_idx_map.clear()
                        idx_array = []
                        break
                    
        elif idx_array and len(idx_array) < 2:
            num_idx_map.clear()
        
    print(final_count)
                

with open('./inputs/day3.txt', 'r') as f:
    for line in f:
        grid += line
        
    char_array = [list(line) for line in grid.strip().split('\n')]
    
    construct_grid_numbers(char_array)
    
    # for row, line in enumerate(char_array):
    #     for col, _ in enumerate(line):
    #         current_char = line[col]
            
    #         if current_char.isdigit():
    #             num += current_char
                
    #             # finding first adjacent number set
    #             if check_adjacency(row, col, char_array):
    #                 row_icon, col_icon = check_adjacency(row, col, char_array)
                    
    #                 # check adjacency of gear (*) icon, return 
    #                 if check_adjacency(row_icon, col_icon, char_array):
    #                     print()
                        
    #         else:
    #             num = ""
            
            # store first encounter, and last encounter before '.' found
            
            
            
        # approach: find indexes of special characters using regex, evaluate the numbers around them
        # if adjacent, multiply them and cumulative sum all adjacent numbers together
        # note: to be adjacent, the row diff = 1 and/or col diff = 1