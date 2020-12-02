
def main():
    with open('input') as f:
        items = f.read()

    data = items.split('\n')
    data.remove('')

    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                di = int(data[i])
                dj = int(data[j])
                dk = int(data[k])
                if di + dj + dk == 2020:
                    print(di * dj * dk)
                    return 0

if __name__ == "__main__":
    main()
