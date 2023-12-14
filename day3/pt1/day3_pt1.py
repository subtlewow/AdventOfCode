import re

pattern = r'[^a-zA-Z0-9\.]' # only look for special chars, excluding '.' chars
elem_count = 0

grid = ""
num = ""
found = False

def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def process_digit(row, col, char_array):
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
    
    for (r, c) in directions.values():
        if is_valid_position(r, c, max_row, max_col):
            match = re.match(pattern, char_array[r][c])
            if match:
                return True
    
    return False
    
with open('day3.txt', 'r') as f:    
    # generates 2D array 
    for row, line in enumerate(f):
        grid += line

    char_array = [list(line) for line in grid.strip().split('\n')]
    
    for row, line in enumerate(char_array):
        num = ""
        found = False
        
        for col, _ in enumerate(line):
            current_char = line[col]
            if current_char.isdigit():
                num += current_char

                # if found, adjacent character is found, no need to update `found` var
                if not found and process_digit(row, col, char_array):
                    found = True
                
                # check if number at end of line
                is_last_col = (col == len(line)-1)
                next_char_not_digit = (col + 1 < len(line) and not line[col+1].isdigit())
                
                if found and (is_last_col or next_char_not_digit):
                    elem_count += int(num)
                    num = ""
                    found = False
                elif not found and next_char_not_digit and line[col+1] == '.':
                    num = ""
                
            else:
                found = False
    
    # correct output: 528799
    print(f"Sum of all part numbers: {elem_count}")