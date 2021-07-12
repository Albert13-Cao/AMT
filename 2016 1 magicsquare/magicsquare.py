with open("magicin.txt") as filein:
    line = filein.readline()
    numbers = line.split()

    row1 = str(numbers[0]) + " " + str(numbers[1]) + " " + str(numbers[2])
    row2 = str(numbers[2]) + " " + str(numbers[0]) + " " + str(numbers[1])
    row3 = str(numbers[1]) + " " + str(numbers[2]) + " " + str(numbers[0])
    # print(line)

with open("magicout.txt", "w") as fileout:
    fileout.write(row1 + "\n" + row2 + "\n" + row3)