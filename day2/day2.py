class Row:
    def __init__(self, min, max, char, passwd):
        self.min = min
        self.max = max
        self.char = char
        self.passwd = passwd

    def valid(self):
        count = self.passwd.count(self.char)
        return count >= self.min and count <= self.max

    def valid2(self):
        a = self.passwd[self.min - 1] == self.char
        b = self.passwd[self.max - 1] == self.char
        return a ^ b

def parse(s):
    a = s.split(':')
    b = a[0].split('-')
    min = int(b[0])
    c = b[1].split(' ')
    max = int(c[0])
    char = c[1]
    passwd = a[1].strip(' ')
    return Row(min, max, char, passwd)

def main():
    with open('input', 'rt') as f:
        data = f.read()

    items = data.splitlines()
    validCount = 0
    valid2Count = 0
    for i in items:
        row = parse(i)
        if row.valid():
            validCount += 1
        if row.valid2():
            valid2Count += 1

    print(validCount)
    print(valid2Count)

if __name__ == '__main__':
    main()
