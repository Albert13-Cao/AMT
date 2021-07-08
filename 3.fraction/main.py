with open("mixin.txt") as mixin:
    line = mixin.readlines()
    numbers = line[0]
    num_list = numbers.split(" ")
    divident = int(num_list[0])
    divisor = int(num_list[1])
    whole = str(divident//divisor)
    # print(whole)
    remainder = divident % divisor

    if remainder == 0:
        answer = whole
    else:
        fraction = str(remainder) + "/" + str(divisor)
        answer = whole + " " + fraction

    # print(answer)
    # print(type(answer))

    with open("mixout.txt", "w") as mixout:
        mixout.write(answer)