grid = []

from collections import defaultdict


def parse_grid_from_file(filename: str):
    '''
    Parses grid input and returns 2D array
    '''
    
    with open(filename, 'r') as f:
        return [[c for c in line.strip('\n')] for line in f]
    

filename = './inputs/day3-3.txt'
grid = parse_grid_from_file(filename)
R = len(grid)
C = len(grid[0])
# gears = set()
nums = defaultdict(list)
p1 = 0
final = 0

for r in range(R):
    n = 0
    gears = set()
    has_part = False
    for c in range(C+1):
        if c < C and grid[r][c].isdigit():
            n = n*10 + int(grid[r][c]) # construct number

            # check adjacency
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r+rr < R and 0 <= c+cc < C: # check if valid position
                        adj_elem = grid[r+rr][c+cc]
                        
                        if adj_elem and adj_elem != '.':
                            has_part = True
                        
                        if adj_elem == '*':
                            gears.add((r+rr, c+cc))
        
        elif n > 0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                p1 += n
            
            n = 0
            has_part = False
            gears = set()

for num in nums.values():
    if len(num) == 2:
        final += (num[0] * num[1])

print(nums)
print(final)