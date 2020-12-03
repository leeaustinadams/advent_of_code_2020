
def traverse(down, right, lines):
    x = 0
    hits = 0
    for l in range(0, len(lines), down):
        line = lines[l]
        if line[x % len(line)] == '#':
            hits += 1
        x += right

    return hits

def main():
    with open('input', 'rt') as f:
        lines = f.read().splitlines()

    a = traverse(1, 1, lines)
    b = traverse(1, 3, lines)
    c = traverse(1, 5, lines)
    d = traverse(1, 7, lines)
    e = traverse(2, 1, lines)

    print(a * b * c * d * e)

if __name__ == '__main__':
    main()
