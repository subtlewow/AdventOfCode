filename = './inputs/day5.txt'

seeds, *blocks = open(filename, 'r').read().split('\n\n')

# parse first line of input ie. seeds
seeds = list(map(int, seeds.split(':')[1].split()))
seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

print(seeds)
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    while len(seeds) > 0:
        start, end = seeds.pop()
        
        for dest_st, src_st, range_len in ranges:
            # finding intersection ie. overlap
            os = max(start, src_st) # overlap start
            oe = min(end, src_st + range_len) # overlap end
            
            if os < oe:
                new.append((os - src_st + dest_st, oe - src_st + dest_st))

        
        
print(ranges)

                
        
        

