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
                    text = line[0].strip(':')
                
                # hash input requirements and numbers_to_query in a map
                if len(line[1:]) > 3:
                    numbers_to_query = list(map(int, line[1:]))
                else:
                    dest_start, source_start, range_len = list(map(int, line)) # seed-to-soil
                    
                    for i in range(range_len):
                        iter_map[source_start + i] = dest_start + i
                    
                    # dest_values.extend(range(dest_start, dest_start + range_len))
                    # source_values.extend(range(source_start, source_start + range_len))
        else:
            query_chain = []
            for num in numbers_to_query:
                query_chain.append(iter_map.get(num, num))
                
            numbers_to_query = query_chain
            iter_map = defaultdict(int)
            
        print(text, numbers_to_query)

        #     # constructs hashmap for source-dest pairs
        #     if dest_values and source_values:
        #         zipped_pairs = sorted(zip(source_values, dest_values))
        #         sorted_dest_values = {source: dest for source, dest in zipped_pairs}
                
        #         for num in numbers_to_query:
        #             if num in dest_values or num in source_values:
        #                 query_chain.append(sorted_dest_values[num])
        #             else:
        #                 query_chain.append(num)

        #         numbers_to_query = query_chain
            
        #     dest_values = []
        #     source_values = []
        #     query_chain = []
        
# process the last batch of data after the loop
# if dest_values and source_values:
#     zipped_pairs = sorted(zip(source_values, dest_values))
#     sorted_dest_values = {source: dest for source, dest in zipped_pairs}

query_chain = []
for num in numbers_to_query:
    query_chain.append(iter_map.get(num, num))
numbers_to_query = query_chain

print("Lowest location number: {}".format(min(numbers_to_query)))
    
#         if num in dest_values or num in source_values:
#             query_chain.append(sorted_dest_values[num])
#         else:
#             query_chain.append(num)

#     numbers_to_query = query_chain

# print(text, numbers_to_query)  # Final output after the last processing
# print("Lowest location number: {}".format(min(numbers_to_query)))