with open("rainin.txt") as rainin:
    lines = [line.rstrip() for line in rainin]
    info = lines[0].split(" ")
    days_of_rain = int(info[0])
    tank_liters = int(info[1])
    # print(lines, tank_liters, days_of_rain)
    lines.remove(lines[0])
    # print(lines)
    days = 0
    water = 0

    for i in range(days_of_rain):
        if water >= tank_liters:
            break
        else:
            water += int(lines[i])
            days += 1
    print(days)

    with open("rainout.txt", "w") as rainout:
        rainout.write(str(days))
