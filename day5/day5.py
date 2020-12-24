# boardingpass = 'BFFFBBFRRR'
def totalrows(start, end):
    x = 1
    for i in range(int(start) + 1, int(end) + 1):
        x += 1
    return x
    
def halvsies(half, start, end):
    mylist = [start, end]
    length = totalrows(mylist[0], mylist[1])
    if half == 'F' or half == 'L':
        mylist[1] = mylist[1] - length / 2
    elif half == 'B' or half == 'R':
        mylist[0] = mylist[0] + length / 2
    return mylist

def seatid(boardingpass):
    rows = [0, 127]
    seats = [0, 7]

    for i in range(7):
        rows = halvsies(boardingpass[i], rows[0], rows[1])
    row = int(rows[0])

    for i in range(7,10):
        seats = halvsies(boardingpass[i], seats[0], seats[1])
    seat = int(seats[0])

    return row * 8 + seat

seatids = []
with open("day5/day5.txt", "r") as f:
    for line in f:
        seatids.append(seatid(line.removesuffix('\n')))

print(sorted(seatids))