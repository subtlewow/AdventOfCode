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
    
    for _, (r, c) in directions.items():
        if is_valid_position(r, c, max_row, max_col):
            match = re.match(pattern, char_array[r][c])
            if match:
                return True
    
    return False

with open('./day3/day3.txt', 'r') as f:
    for line in f:
        grid += line
        
    char_array = [list(line) for line in grid.strip().split('\n')]
    
    for row, line in enumerate(char_array):
        for col, _ in enumerate(line):
            
            
        # approach: find indexes of special characters using regex, evaluate the numbers around them
        # if adjacent, multiply them and cumulative sum all adjacent numbers together