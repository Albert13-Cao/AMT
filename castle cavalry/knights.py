with open("cavalryin.txt") as filein:
    cavalry_dict = {}
    current_line = 1
    num_of_knights = 0
    for line in filein:
        if current_line == 1:
            num_of_knights = int(line)
        else:
            group_knights = int(line)
            try:
                cavalry_dict[int(line)] += 1
            except KeyError:
                cavalry_dict[int(line)] = 1
        current_line += 1

    result = "YES"
    for key in cavalry_dict.keys():
        if cavalry_dict[key] % key == 0:
            pass
        else:
            result = "NO"
            continue

with open("cavalryout.txt", "w") as fileout:
    fileout.write(result)