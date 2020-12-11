
def check_for_sum(numbers, number):
    for x in range(0, len(numbers)):
        for y in range(0, len(numbers)):
            if x != y:
                if numbers[x] + numbers[y] == number:
                    return True

    return False

def main():

    with open('input', 'rt') as f:
        data = f.read()

    numbers = [int(x) for x in data.splitlines()]
    queue = []

    for i in range(0, len(numbers)):
        number = numbers[i]

        if i >= 25:
            if not check_for_sum(queue, number):
                print(number)
                return

            queue.pop(0)

        queue.append(number)

if __name__ == '__main__':
    main()
