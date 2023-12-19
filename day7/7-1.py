from collections import Counter, defaultdict

filename = './inputs/7.txt'
D = open(filename, 'r').read().split('\n')

hands, bids = zip(*[d.split() for d in D])
bids = list(map(int, bids))

print(hands, bids)

ranks = defaultdict(list)

occur = 0
final = 0

for i, h in enumerate(hands):
    count = Counter(h)
    count_occur = Counter(count.values())
    
    print(count_occur)
    
    # five of a kind
    key_len = len(count_occur.keys())
    val_len = len(count_occur.values())
    
    max_key = max(count_occur.keys())
    max_val = max(count_occur.values())
    
    if key_len == 1 and val_len == 1:
        if max_key > max_val:
            rank = 7
        else:
            rank = 0
    elif max_key == 2:
        if count_occur[max_key] == 1:
            rank = 2
            
            if i == 0:
                rank = 1
        elif count_occur[max_key] == 2:
            rank = 3
    elif max_key == 3 and count_occur[max_key] == 1:
        if len(set(h)) == 3:
            rank = 4
        elif len(set(h)) == 2:
            rank = 5
    elif max_key == 4:
        rank = 6
    
    # comparing characters to determine dominant rank
    if len(ranks[rank]) == 1:
        elem = ranks[rank][0]
        for j in range(len(h)):
            if ord(h[j]) > ord(elem[j]):
                final += (bids[i] * (rank-1))
                print(h, bids[i], rank-1, final)
                break
            elif ord(h[j]) < ord(elem[j]):
                final += (bids[i] * (rank+1))
                print(bids[i], rank+1, final)
                break
    else:
        ranks[rank].append(h)
        final += (bids[i] * rank)
        print(h, bids[i], rank, final)

print(ranks, final)
 