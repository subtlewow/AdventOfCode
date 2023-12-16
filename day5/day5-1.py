# (destination start, source start, range) - gives a subset of entire data, then extrapolate to fit entire data from 0 -> n

# ie. seed-to-soil then (soil start, seed start, range)
from collections import defaultdict

mapping = defaultdict(list)
iter_map = defaultdict(int)

with open('./inputs/day5.txt', 'r') as f:
    numbers_to_query = []
    source_ls = []
    dest_values = []
    source_values = []
    query_chain = []
    for i, line in enumerate(f):
        line = line.strip('\n').split()
        
        # finding source-destination input, and number query
        if line:
            if line[1] == 'map:':
                text = line[0]
            else:
            # parsing first line ie. 'seeds: etc..' 
                if not line[0].isdigit():
                    text = line[0].strip('s:')
                
                # hash input requirements and numbers_to_query in a map
                if len(line[1:]) > 3:
                    numbers_to_query = list(map(int, line[1:]))
                else:
                    dest_start, source_start, range_len = list(map(int, line)) # seed-to-soil
                    
                    dest_values.extend(range(dest_start, dest_start + range_len))
                    source_values.extend(range(source_start, source_start + range_len))
        else:
            # constructs hashmap for source-dest pairs
            if dest_values and source_values:
                zipped_pairs = sorted(zip(source_values, dest_values))
                sorted_dest_values = {source: dest for source, dest in zipped_pairs}
                
                for num in numbers_to_query:
                    if num in dest_values or num in source_values:
                        query_chain.append(sorted_dest_values[num])
                    else:
                        query_chain.append(num)

                numbers_to_query = query_chain
                
            print(numbers_to_query)
                        
        
    