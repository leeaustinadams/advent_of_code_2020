import sys

def find_adapter(jolts, adapters, difference):
    for adapter in adapters:
        if adapter - jolts == difference:
            return adapter

    return None

def find_adapters(start_jolts, adapters):
    jolts = start_jolts
    output = []
    diffs_of_1 = 0
    diffs_of_3 = 0

    while len(output) < len(adapters):

        adapter = find_adapter(jolts, adapters, 1)
        if adapter:
            diffs_of_1 += 1
            output.append(adapter)
            jolts = adapter
            continue

        adapter = find_adapter(jolts, adapters, 2)
        if adapter:
            output.append(adapter)
            jolts = adapter
            continue

        adapter = find_adapter(jolts, adapters, 3)
        if adapter:
            diffs_of_3 += 1
            output.append(adapter)
            jolts = adapter
            continue

        # No suitable adapter found
        return None

    return (output, diffs_of_1, diffs_of_3)

def main(filename):
    with open(filename, 'rt') as f:
        data = f.read()

    adapters = [int(x) for x in data.splitlines()]
    adapters.sort()
    largest = max(adapters)

    adapters.append(largest + 3)

    answers = []
    answer = find_adapters(0, adapters)
    if answer:
        answers.append(answer)

    for i in range(0, len(adapters)):
        a = adapters.copy()
        a.pop(i)
        answer = find_adapters(0, a)
        if answer:
            answers.append(answer)

    for answer in answers:
        print(answer)

    print("Answers:", len(answers))

if __name__ == '__main__':
    main(sys.argv[1])
