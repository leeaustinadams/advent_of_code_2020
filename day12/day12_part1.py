import sys
import re

pattern = re.compile(r'(N|S|E|W|L|R|F)(\d+)')

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 'E'

    def update(self, dir, count):
        self.move_forward(dir, count)

        if dir == 'F':
            self.move_forward(self.dir, count)
        elif dir == 'R':
            while count > 0:
                self.turn_clockwise()
                count -= 90
        elif dir == 'L':
            while count > 0:
                self.turn_counterclockwise()
                count -= 90

    # Does nothing if the dir is not N, E, W, or S
    def move_forward(self, dir, count):
        if dir == 'E':
            self.x += count
        elif dir == 'S':
            self.y -= count
        elif dir == 'W':
            self.x -= count
        elif dir == 'N':
            self.y += count

    def turn_clockwise(self):
        if self.dir == 'E':
            self.dir = 'S'
        elif self.dir == 'S':
            self.dir = 'W'
        elif self.dir == 'W':
            self.dir = 'N'
        elif self.dir == 'N':
            self.dir = 'E'

    def turn_counterclockwise(self):
        if self.dir == 'E':
            self.dir = 'N'
        elif self.dir == 'S':
            self.dir = 'E'
        elif self.dir == 'W':
            self.dir = 'S'
        elif self.dir == 'N':
            self.dir = 'W'

    def print(self):
        print(self.x, 'x', self.y)

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    lines = data.splitlines()

    s = Ship()
    for line in lines:
        dir, count = pattern.match(line).groups()
        s.update(dir, int(count))

    s.print()

if __name__ == '__main__':
    main(sys.argv[1])
