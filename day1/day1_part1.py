
def main():
    with open('input') as f:
        items = f.read()

    data = items.split('\n')
    data.remove('')

    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            di = int(data[i])
            dj = int(data[j])
            if di + dj == 2020:
                print(di * dj)
                return 0

if __name__ == "__main__":
    main()
