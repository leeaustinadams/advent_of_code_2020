
def getSeatId(code):
    rows = list(range(0, 128))
    cols = list(range(0, 8))

    print(code)

    for c in code:
        if c == 'F':
            l = len(rows)
            s = int(l / 2)
            rows = rows[0:s]
        elif c == 'B':
            l = len(rows)
            s = int(l / 2)
            rows = rows[s:l]
        elif c == 'L':
            l = len(cols)
            s = int(l / 2)
            cols = cols[0:s]
        elif c == 'R':
            l = len(cols)
            s = int(l / 2)
            cols = cols[s:l]

    print('Row:', rows[0], 'Col:', cols[0])
    result = (rows[0] * 8) + cols[0];
    print(result)

    return result

def findSeat(seatIds):
    seatIds.sort()

    for seat in range(0, 8 * 128):
        if seat not in seatIds:
            if (seat - 1) in seatIds and (seat + 1) in seatIds:
                return seat

    return -1

def main():
    with open('input', 'rt') as f:
        data = f.read()

    codes = data.splitlines()

    highestSeatId = 0

    seatIds = []
    for code in codes:
        seatId = getSeatId(code)
        seatIds.append(seatId)
        if seatId > highestSeatId:
            highestSeatId = seatId

    print(highestSeatId)

    print(findSeat(seatIds))

if __name__ == '__main__':
    main()
