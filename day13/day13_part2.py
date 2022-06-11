import sys

def find(timestamp, ids):
    for i in range(0, len(ids)):
        id = ids[i]
        if id != 'x':
            value = int(id)
            if (timestamp + i) % value != 0:
                return False

    return True

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    ids = data.split(',')

    print(ids)

    timestamp = int(ids[0])
    found = False
    while not found:
#        print(timestamp)
        found = find(timestamp, ids)
        timestamp += int(ids[0])

    print(timestamp)

if __name__ == '__main__':
    main(sys.argv[1])
