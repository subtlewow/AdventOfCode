
final_elem_cnt = {}
key = 0
value = 0
config = {'red': 12, 'green': 13, 'blue': 14}
true_valid = 1
total_id = 0
with open('day2.txt', 'r') as f:
    for line in f:
        s = line.strip('\n')
        
        # processing string
        elements = s.split(':')[1].split(';')
        game_id = s.split(':')[0].split(' ')[1]
        final_elem_cnt[game_id] = []
        
        valid = 0
        indv_elem_case = 0
        
        # seperating elements and count into map
        for i in range(len(elements)):
            element = elements[i].strip(' ').split(' ')
            
            j = 0
            
            # hashmap of individual element counts
            while j < len(element):
                if j % 2 == 0:
                    value = int(element[j])
                    key = element[j+1].strip(',')
                
                # comparison against criteria configuration
                if key in config:
                    if value <= config[key]:
                        true_valid = 1
                        valid = 1
                    else:
                        valid = 0
                
                if not valid:
                    true_valid = 0
                    break
                
                j += 2
            
            if true_valid:
                final_elem_cnt[game_id].append(true_valid)
            else:
                final_elem_cnt[game_id] = []
                break
            
        if true_valid and all(n == 1 for n in final_elem_cnt[game_id]):
            total_id += int(game_id)
        
    print(final_elem_cnt, total_id)