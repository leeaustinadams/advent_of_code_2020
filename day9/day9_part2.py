
def check_for_sum(numbers, number):
    for x in range(0, len(numbers)):
        for y in range(0, len(numbers)):
            if x != y:
                if numbers[x] + numbers[y] == number:
                    return True

    return False

def find_invalid_number(numbers, preamble_length):
    queue = []

    for i in range(0, len(numbers)):
        number = numbers[i]

        if i >= preamble_length:
            if not check_for_sum(queue, number):
                return (True, number)

            queue.pop(0)

        queue.append(number)

    return (False, None)

def find_contiguous_sum(numbers, number):

    queue = list()

    for n in numbers:
        queue.append(n)

        group_sum = sum(queue)
        print(group_sum, ':', queue)

        if group_sum == number:
            return queue
        else:
            while len(queue) > 0 and group_sum > number:
                queue.pop(0)
                group_sum = sum(queue)
                if group_sum == number:
                    return queue

    return None

def main():

    with open('input', 'rt') as f:
        data = f.read()

    numbers = [int(x) for x in data.splitlines()]

    found, invalid_number = find_invalid_number(numbers, 25)

    if found:
        print(invalid_number)

        group = find_contiguous_sum(numbers, invalid_number)

        print(group)
        print(min(group) + max(group))

if __name__ == '__main__':
    main()
