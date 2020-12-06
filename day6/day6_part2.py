
def main():
    with open('input', 'rt') as f:
        data = f.read()

    groups = data.split('\n\n')

    sum = 0

    for group in groups:
        individual = group.splitlines()
        groupCount = len(individual)
        yes = {}
        for answers in individual:
            for answer in answers:
                if answer in yes:
                    yes[answer] = yes[answer] + 1
                else:
                    yes[answer] = 1

        allYes = len(list(filter(lambda x: x == groupCount, yes.values())))

        sum += allYes

    print(sum)

if __name__ == '__main__':
    main()
