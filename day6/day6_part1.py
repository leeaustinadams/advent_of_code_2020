
def main():
    with open('input', 'rt') as f:
        data = f.read()

    groups = data.split('\n\n')

    sum = 0

    for group in groups:
        individual = group.splitlines()
        yes = set()
        for answers in individual:
            for answer in answers:
                yes.add(answer)

        sum += len(yes)

    print(sum)

if __name__ == '__main__':
    main()
