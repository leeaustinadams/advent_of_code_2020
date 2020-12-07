import re

def sum_recursive(bags, color):
    print(color)
    sub_bags = bags[color]
    value = 0
    if len(sub_bags) > 0:
        print(sub_bags)
        for sub_count, sub_color in sub_bags:
            count = int(sub_count)
            value += count + (count * sum_recursive(bags, sub_color))

    return value

def main():

    with open('input', 'rt') as f:
        data = f.read()

    rules = data.splitlines()

    headRe = re.compile(r'([a-z ]+) bags')
    restRe = re.compile(r'(\d+) ([a-z ]+) bags?')

    bags = {}
    for rule in rules:
        head, rest = rule.split(' contain ')
        m = headRe.match(head)
        headColor = m.groups()[0]
        restColors = []
        for r in rest.split(', '):
            if r != 'no other bags.':
                m = restRe.match(r)
                restColors.append(m.groups())
        bags[headColor] = restColors

    bags_sum = sum_recursive(bags, 'shiny gold')
    print(bags_sum)

if __name__ == '__main__':
    main()
