with open('input', 'rt') as f:
    lines = f.read().splitlines()

x = 0
hits = 0
for l in lines:
    if l[x % len(l)] == '#':
        hits += 1
    x += 3

print(hits)
