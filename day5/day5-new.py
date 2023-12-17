file_input = './inputs/day5.txt'

seeds, *blocks = open(file_input).read().split('\n\n')
seeds = list(map(int, seeds.split(': ')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    
    mapp = []
    for query in seeds:
        for dest_start, source_start, range_len in ranges:
            if source_start <= query < source_start + range_len:
                mapp.append(query - source_start + dest_start)
                break
        else:
            mapp.append(query)
        
    seeds = mapp

print(min(seeds))