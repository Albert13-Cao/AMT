with open("countin.txt") as countin:
    number_list = countin.readlines()
    number = int(number_list[0])

    with open("countout.txt", "a") as countout:
        for i in range(1, number + 1):
            # print(i)
            if i != number:
                countout.write(str(i) + "\n")
            else:
                countout.write(str(i))
            i += 1

