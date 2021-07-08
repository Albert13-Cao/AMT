with open("addin.txt") as file:
    lines = file.readlines()
    # print(lines)
    numbers = lines[0]
    number_list = numbers.split()
    # print(number_list)
    num_1 = int(number_list[0])
    num_2 = int(number_list[1])
    sum = num_1 + num_2
    with open("addout.txt", "a") as file_2:
        file_2.write(str(sum))
