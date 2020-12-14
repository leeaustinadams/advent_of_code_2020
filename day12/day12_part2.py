import sys
import re
import math

pattern = re.compile(r'(N|S|E|W|L|R|F)(\d+)')

def rotate_2d(position, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    x, y = position
    x_prime = (x * cos_theta) - (y * sin_theta)
    y_prime = (y * cos_theta) + (x * sin_theta)

    return (x_prime, y_prime)

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 'E'
        self.waypoint_x = 10
        self.waypoint_y = 1

    def update(self, dir, count):
        self.move_waypoint(dir, count)

        if dir == 'F':
            self.move_toward_waypoint(count)
        elif dir == 'R':
            self.rotate_waypoint(360-count)
        elif dir == 'L':
            self.rotate_waypoint(count)

    def move_toward_waypoint(self, count):
        self.x = self.x + (count * self.waypoint_x)
        self.y = self.y + (count * self.waypoint_y)

    # Does nothing if the dir is not N, E, W, or S
    def move_waypoint(self, dir, count):
        if dir == 'E':
            self.waypoint_x += count
        elif dir == 'S':
            self.waypoint_y -= count
        elif dir == 'W':
            self.waypoint_x -= count
        elif dir == 'N':
            self.waypoint_y += count

    def rotate_waypoint(self, count):
        theta = math.radians(count)
        self.waypoint_x, self.waypoint_y = rotate_2d((self.waypoint_x, self.waypoint_y), theta)

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
        print(self.x, 'x', self.y, ':', self.waypoint_x, 'x', self.waypoint_y)

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    lines = data.splitlines()

    s = Ship()
    s.print()

    for line in lines:
        dir, count = pattern.match(line).groups()
#        print(dir, count)
        s.update(dir, int(count))
#        s.print()

    s.print()
if __name__ == '__main__':
    main(sys.argv[1])
