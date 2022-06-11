import sys

def next_departure(timestamp, id):
    count = 1
    next = id

    while next < timestamp:
        next = id * count
        count += 1

    return next

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    timestamp, ids = data.splitlines()
    timestamp = int(timestamp)
    ids = [int(x) for x in ids.split(',') if x != 'x']

    departures = [next_departure(timestamp, id) for id in ids]

    print(ids)
    print(departures)
    print(min(departures))

if __name__ == '__main__':
    main(sys.argv[1])
