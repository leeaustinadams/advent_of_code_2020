
def parse(data):
    items = data.split('\n\n')
    items = [x.replace('\n', ' ') for x in items]
    items = [x.split(' ') for x in items]

    records = []
    for item in items:
        pairs = [s.split(':') for s in item];
        record = {}
        for pair in pairs:
            if len(pair) == 2:
                record[pair[0]] = pair[1]
        records.append(record)

    return records

def valid(record, keys):
    for k in keys:
        if k not in record:
            return False

    return True

def main():
    with open('input', 'rt') as f:
        data = f.read()

    records = parse(data)
    validCount = 0

    print('Record count: ', len(records))

    keys = ['byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid']

    for record in records:
        if valid(record, keys):
            validCount += 1

    print(validCount)

if __name__ == '__main__':
    main()
