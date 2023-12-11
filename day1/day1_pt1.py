import os
import sys

sys.path.append(os.getcwd())

import input_parser

puzzle_input = input_parser.input_parser('day1')
count = 0
new = ""

for line in puzzle_input:
    new = ""
    
    for i, char in enumerate(line):
        ascii_val = ord(char)

        if (48 <= ascii_val <= 57):
            if len(new) >= 2:
                new = str(int(new) // 10)
            new += char
        
    if len(new) == 1:
        new = new * 2
        
    if new:
        count += int(new)
        
print("The sum of all calibration values: {}".format(count))

