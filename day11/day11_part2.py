import sys

class Board:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.lines = lines

    def print(self):
        for row in self.lines:
            print(row)

    def tick(self):
        new_lines = []
        for row in self.lines:
            new_lines.append(row.copy())

        changes = 0

        for row in range(0, self.height):
            for column in range(0, self.width):
                status = self.status(column, row)
                if status != '.':
                    adj = self.check_dirs(column, row)
                    if status == 'L' and adj == 0:
                        new_lines[row][column] = '#'
                        changes += 1
                    elif status == '#' and adj >= 5:
                        new_lines[row][column] = 'L'
                        changes += 1

        self.lines = new_lines

        return changes

    def check_dirs(self, x, y):
        seen = 0
        if self.check_dir(x, y, 0, -1) == '#':
            seen += 1
        if self.check_dir(x, y, 1, -1) == '#':
            seen += 1
        if self.check_dir(x, y, 1, 0) == '#':
            seen += 1
        if self.check_dir(x, y, 1, 1) == '#':
            seen += 1
        if self.check_dir(x, y, 0, 1) == '#':
            seen += 1
        if self.check_dir(x, y, -1, 1) == '#':
            seen += 1
        if self.check_dir(x, y, -1, 0) == '#':
            seen += 1
        if self.check_dir(x, y, -1, -1) == '#':
            seen += 1

        return seen

    def check_dir(self, x, y, delta_x, delta_y):
        x += delta_x
        y += delta_y

        while x >= 0 and x < self.width and y >= 0 and y < self.height:
            status = self.status(x, y)
            if status == 'L':
                return 'L'
            elif status == '#':
                return '#'

            x += delta_x
            y += delta_y

        return None

    def status(self, x, y):
        row = self.lines[y]
        return row[x]


    def check_adjacent(self, x, y):
        occupied = 0
        occupied += self.check_above_and_below(x, y)

        if x > 0:
            occupied += self.check_above_and_below(x - 1, y)
            if self.status(x - 1, y) == '#':
                occupied += 1

        if x < self.width - 1:
            occupied += self.check_above_and_below(x + 1, y)
            if self.status(x + 1, y) == '#':
                occupied += 1

        return occupied

    def check_above_and_below(self, x, y):
        occupied = 0
        if y > 0:
            if self.status(x, y - 1) == '#':
                occupied += 1

        if y < self.height - 1:
            if self.status(x, y + 1) == '#':
                occupied += 1

        return occupied

    def occupancy(self):
        occupied = 0
        for row in self.lines:
            for seat in row:
                if seat == '#':
                    occupied += 1

        return occupied

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    lines = data.splitlines()
    board = []
    for line in lines:
        board_line = []
        for c in line:
            board_line.append(c)

        board.append(board_line)

    b = Board(board)

    b.print()

    changes = 1
    while changes > 0:
        changes = b.tick()

        print(changes, ':')
        b.print()

    print('Occupancy:', b.occupancy())

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
