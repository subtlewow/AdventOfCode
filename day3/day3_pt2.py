import re

pattern = r'\*' # only look for special chars, excluding '.' chars
elem_count = 0

grid = ""
num = ""
found = False

def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def is_adjacent(row, col, char_array):
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
    
    for _, (r, c) in directions.items():
        if is_valid_position(r, c, max_row, max_col):
            match = re.match(pattern, char_array[r][c])
            if match:
                return True
    
    return False

def construct_grid_numbers(char_array, num=""): 
    first = False 
    last = False 
    
    first_idx = -1
    last_idx = -1 
    
    adjacent = False
    
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
                
                if is_adjacent(row, col, char_array):
                    adjacent = True
                
                if col+1 < len(line) and not line[col+1].isdigit():
                    last = True
                    last_idx = col
            else:
                if current_char == '*':
                    if current_char not in num_idx_map:
                        num_idx_map[current_char] = [row, [row, col]]
                    else:
                        num_idx_map[current_char].append([row, [row, col]])
                
                first_idx, last_idx = -1, -1
                adjacent = False
                first = False
                last = False
                num = ""
            
            if first and last and adjacent:
                num_idx_map[num] = [row, [first_idx, last_idx]]
                
            
                
            
            
            
        
        
            
                

with open('./inputs/day3.txt', 'r') as f:
    for line in f:
        grid += line
        
    char_array = [list(line) for line in grid.strip().split('\n')]
    
    tmp = [[] for _ in range(len(char_array))]
    
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