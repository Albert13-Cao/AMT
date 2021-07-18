with open("archin.txt") as filein:
    best = 0
    worst = 0
    info = filein.readline().split()
    print(info)
    people_participating = int(info[0])
    first_day_place = int(info[1])
    second_day_place = int(info[2])
    
    first_greater = first_day_place - 1
    first_less = people_participating - first_day_place
    second_greater = second_day_place - 1
    second_less = people_participating - second_day_place
    print(first_greater, first_less, second_greater, second_less)

    best = min(first_day_place, second_day_place, abs(first_greater - second_less) + 1, abs(second_greater - first_less) + 1)
    worst = min(first_greater + second_greater + 1, people_participating)
    print(best, worst)

with open("archout.txt", "w") as fileout:
    fileout.write(str(best) + " " + str(worst))