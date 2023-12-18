import math

x = open('./inputs/day6.txt').read().split('\n')
z = [int("".join(xi.split(':')[1].split())) for xi in x]

t, d = z
c = 0

# pq formula x2 - px + q = 0
x1 = math.ceil((-t / 2) - math.sqrt((t**2) / 4 - d))
x2 = math.floor((-t / 2) + math.sqrt((t**2) / 4 - d))

print(x2-x1+1)