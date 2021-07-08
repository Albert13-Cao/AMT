with open("taktakin.txt") as taktakin:
    numbers = taktakin.readlines()
    number = int(numbers[0])
    answer1 = 0
    isdone = False

    while isdone == False:
        if number % 11 == 1:
            isdone = True
        else:
            number *= 2
            answer1 += 1

    answer = str(answer1) + " " + str(number)

    with open("taktakout.txt", "w") as taktakout:
        taktakout.write(answer)