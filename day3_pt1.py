import re

pattern = r'[^a-zA-Z0-9\.]'
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
    
with open('day3.txt', 'r') as f:    
    # generates 2D array 
    for row, line in enumerate(f):
        grid += line

    char_array = [list(line) for line in grid.strip().split('\n')]
    
    for row, line in enumerate(char_array):
        num = ""
        found = False
        for col, char in enumerate(line):
            if char_array[row][col].isdigit():
                num += char_array[row][col]
                results = process_digit(row, col, char_array)
                
                if results:
                    found = True
                
                if found and not char_array[row][col+1].isdigit():
                    elem_count += int(num)
                    num = ""
                elif col+1 < len(char_array[row]) and not found and char_array[row][col+1] == '.':
                    num = ""
            else:
                found = False
                
                
                # if col < len(char_array[row])-1:
                #     DOWN = re.match(pattern, char_array[row+1][col])
                #     RIGHT = re.match(pattern, char_array[row][col+1])
                #     LR = re.match(pattern, char_array[row+1][col+1])
                    
                #     if DOWN or RIGHT or LR:
                #         elem_count += int(num)
                #         num = ""
                #     elif not (DOWN or RIGHT or LR) and char_array[row][col+1] == '.':
                #         num = ""
                # elif col > 0 and row == 0:
                #     LEFT 
                #     LL
                #     DOWN
                #     LR
                #     RIGHT    
                
                    
                # else:
                #     DOWN = re.match(pattern, char_array[row+1][col])
                #     LL = re.match(pattern, char_array[row+1][col-1])    
                    
                #     if LL or DOWN:
                #         elem_count += int(num)
                #         num = ""
                #     elif not (DOWN or LL) and char_array[row+1][col] == '.':
                #         num = ""
                
                
                # elif row == len(char_array)-1:
                #     # UP = re.match(pattern, line[row+1][col])
                #     # RIGHT = re.match(pattern, line[row][col+1])
                #     
                
                
                # if col == len(line)-1:
                #     # DOWN and LEFT
                #     LEFT = re.match(pattern, line[row][col-1])
                

                
            
            
            # UP = re.match(pattern, line[row+1][col])
            
            # UL = re.match(pattern, line[row-1][col-1])
            
            # if col+1 < len(line):
                
            #     UR = re.match(pattern, line[row-1][col+1])
            
            ## DIAGONALS
            
            
            
            # LL = re.match(pattern, line[row+1][col-1])
            # LR = re.match(pattern, line[row+1][col+1])
            
            
            # if row == 0 and char_array[row][col].isdigit(): # first row then only
            #     print('a')

                
    #             while char_array[row][col+1] != '.': 
    #                 num += char_array[row][col]
    #                 if (LEFT or RIGHT) or (LL or LR) or (DOWN):
    #                     elem_count += int(num)
    #                 print(num)
        
    
    
        
        # for col, char in enumerate(line):
            
#             print(grid[row][col])
            
            
            # check prev rows
            # if row > 0:
            
            # else:
            #     # checking if symbol char
                
            #     ## VERTICAL
            
                    

    
    # for row, line in enumerate(f):
    #     line = line.strip('\n')
        
        # iterating across the row
        # for col, elem in enumerate(line):
        #     if elem.isdigit():
        #         if row > 0:
        #             pass
        #         else:
        #             line[row+1]
                
            
            # print(col, elem)

            
        
        # only need to check for next row
        # if row == 0:
            
        # # only time need to check for previous row
        # if row > 0:
        
        
        # check must be performed for every number encountered
        # once number is encountered, need to check around it for an adjacent symbol that isn't a period symbol
        # need: final moment number is encountered prior to period symbol, store this index
        # index then used for next line iteration
        
        # an index that tracks the row number, n
        # another index that tracks:
            # left: [i-1, j], right: [i+1, j]
            # up: [i, j+1], down: [i, j-1]
            # diagonal UL: [i-1, j+1], diagonal UR: [i+1, j+1]
            # diagonal LL: [i-1, j-1], diagonal LR: [i+1, j-1]
        #