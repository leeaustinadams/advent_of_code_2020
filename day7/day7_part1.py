import re

def search(bags, color):
    colors = []
    for bag, contained_bags in bags.items():
        if color in contained_bags:
            colors.append(bag)

    return colors

def add_recursive(bags, containers, color):
    new_containers = search(bags, color)
    for container in new_containers:
        containers.add(container)
        add_recursive(bags, containers, container)

def main():

    with open('input', 'rt') as f:
        data = f.read()

    rules = data.splitlines()

    headRe = re.compile(r'([a-z ]+) bags')
    restRe = re.compile(r'\d+ ([a-z ]+) bags?')

    bags = {}
    for rule in rules:
        head, rest = rule.split(' contain ')
        m = headRe.match(head)
        headColor = m.groups()[0]
        restColors = []
        for r in rest.split(', '):
            if r != 'no other bags.':
                m = restRe.match(r)
                restColors.append(m.groups()[0])
        bags[headColor] = restColors

    containers = set()
    add_recursive(bags, containers, 'shiny gold')
    print(containers)
    print(len(containers))

if __name__ == '__main__':
    main()
