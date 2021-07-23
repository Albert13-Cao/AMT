with open("cutein.txt") as filein:
    current_line = 1
    num_list = []
    num_digits = 0
    for line in filein:
        if current_line == 1:
            num_digits = int(line)
        else:
            num_list.append(int(line))
        current_line += 1

    answer = 0
    i = -1
    while num_list[i] == 0:
        answer += 1
        i -= 1

with open("cuteout.txt", "w") as fileout:
    fileout.write(str(answer))