with open("sitin.txt") as f:
    lines = [line.rstrip() for line in f]
    # print(lines)
    numbers = lines[0]
    people = int(lines[1])
    num_list = numbers.split(" ")
    row = int(num_list[0])
    column = int(num_list[1])
    seats = row * column
    sitting = 0
    standing = 0

    if people >= seats:
        sitting = seats
        standing = people - seats
    else:
        sitting = people
        standing = 0
    answer = str(sitting) + " " + str(standing)

    with open("sitout.txt", "w") as f2:
        f2.write(answer)