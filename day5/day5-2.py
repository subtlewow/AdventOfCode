# range start, range length

filename = './inputs/day5.txt'
inputs, *blocks = open(filename).read().split('\n\n')

inputs = list(map(int, inputs.split(':')[1].split()))
seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

print(seeds)
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    
    new = []
    
    while len(seeds) > 0:
        s, e = seeds.pop()
        
        for a, b, c in ranges:
            
        # for dest_start, source_start, range_len in ranges:
        #     for val in range(start, end):
        #         if source_start <= val < source_start + range_len: # 98 <= 80 < 100
        #             new.append(val - source_start + dest_start)
        #             break
        #     else:
        #         new.append(val)
                    
    print(new)