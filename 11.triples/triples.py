with open("tripin.txt") as tripin:
    # current_line = 0
    no_quantity = 0
    num_of_numbers = 0
    replacement = "Nothing here!"

    # lines = [line.rstrip() for line in tripin]
    result = []
    for current_line, line in enumerate(tripin):
        # current_line += 1
        # print(current_line)
        if current_line == 1:
            num_of_numbers = int(line)
        else:
            if int(line) % 3 == 0:
                result.append(str(current_line))
        
    with open("tripout.txt", "w") as tripout:
        if result == []:
            tripout.write(replacement)
        else:
            tripout.write(str(len(result)) + "\n")
            tripout.write(" ".join(result))