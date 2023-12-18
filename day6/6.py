
x = open('./inputs/day6.txt').read().split('\n')

z = [xi.split(':')[1].split() for xi in x]

items = [[int(item) for item in inner_ls] for inner_ls in z]
td_pairs = list(zip(*items))

final = 1
for t, d in td_pairs:
    c = 0
    for ti in range(t):
        calc = ti * (t - ti)
        if calc > d:
            c += 1
    
    final *= c
    
print(final)
