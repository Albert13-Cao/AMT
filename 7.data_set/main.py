with open("dishin.txt") as dishin:
    lines = [line.rstrip() for line in dishin]
    # print(lines)
    total = 0
    smallest = 1000001
    largest = 0

    for i in range(1, len(lines)):
        total += int(lines[i])
        if int(lines[i]) < smallest:
            smallest = int(lines[i])
        if int(lines[i]) > largest:
            largest = int(lines[i])

    mean = total // int(lines[0])
    answer = str(smallest) + " " + str(largest) + " " +str(mean)

    with open("dishout.txt", "w") as dishout:
        dishout.write(answer)
