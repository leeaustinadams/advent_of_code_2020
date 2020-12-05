import re

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
    for name, validate in keys.items():
        if name not in record:
            print('Missing: ', name)
            return False
        if not validate(record[name]):
            print(name, record[name])
            return False

    return True

def byr(x):
    value = int(x)
    return value >= 1920 and value <= 2002

def iyr(x):
    value = int(x)
    return value >= 2010 and value <= 2020

def eyr(x):
    value = int(x)
    return value >= 2020 and value <= 2030

hgtRe = re.compile('(\d+)(cm|in)')
def hgt(x):
    m = hgtRe.fullmatch(x)
    if m == None:
        return False
    value, unit = m.groups()
    value = int(value)
    if unit == 'in':
        return value >= 59 and value <= 76
    elif unit == 'cm':
        return value >= 150 and value <= 193
    else:
        return False

hclRe = re.compile('#[0-9a-f]{6}')

def hcl(x):
    return hclRe.fullmatch(x) != None

def ecl(x):
    return x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

pidRe = re.compile('\d{9}')

def pid(x):
    return pidRe.fullmatch(x) != None

def main():
    with open('input', 'rt') as f:
        data = f.read()

    records = parse(data)
    validCount = 0

    print('Record count: ', len(records))

    keys = {'byr': byr,
            'iyr': iyr,
            'eyr': eyr,
            'hgt': hgt,
            'hcl': hcl,
            'ecl': ecl,
            'pid': pid}

    for record in records:
        if valid(record, keys):
            validCount += 1

    print(validCount)

if __name__ == '__main__':
    main()
