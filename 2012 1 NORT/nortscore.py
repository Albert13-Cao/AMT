with open("nortin.txt") as filein:
    info = filein.readline().split()
    row = int(info[0])
    column = int(info[1])
    answer = 0

    if (row * column) % 2 == 0:
        answer = row * column
    else:
        answer = (row * column) - 1

with open("nortout.txt", "w") as fileout:
    fileout.write(str(answer))