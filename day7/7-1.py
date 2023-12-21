from collections import Counter, defaultdict

filename = './inputs/7.txt'
D = open(filename).read().splitlines()

hands = []
bids = []
for line in D:
    hand, bid = line.split()
    hands.append(hand)
    bids.append(bid)

print(hands, bids)

bids = list(map(int, bids))

ranks = []

ordering = ["A", 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_order(elem):
    return ordering.index(elem)

def determine_rank(counts):
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

for i, h in enumerate(hands):
    arr = [h.count(x) for x in h]
    
    rank = determine_rank(arr)
    
    if rank in ranks:
        # compare character strings
        common = hands[ranks.index(rank)]
        print(common)
        
        for j in range(len(h)):

            if get_order(h[j]) > get_order(common[j]): # 4 1
                new_rank = ranks[ranks.index(rank)]
                
                ranks[ranks.index(rank)] += 1
                # while conflict in ranks:
                #     ranks[ranks.index(conflict)] += 1
                #     conflict += 1
                    
                
                
                # ranks[ranks.index(rank)] += 1
                # ranks.append(rank)
                break
            elif get_order(h[j]) < get_order(common[j]): # 1 4 T K
                ranks[ranks.index(rank)] += 1
                ranks.append(rank+2)
                break
            # break
            # if ord(h[j]) > ord(common[j]):
            #     ranks[ranks.index(rank)] += 1
            #     ranks.append(rank)
            #     break
            # elif ord(h[j]) < ord(common[j]):
            #     ranks[ranks.index(rank)] += 1
            #     ranks.append(rank+2)
            #     break
    else:
        ranks.append(rank)
    
    # print(ranks)
total = 0
for i in range(len(bids)):
    total += (bids[i] * ranks[i])

        
            
print(ranks, total)
            
