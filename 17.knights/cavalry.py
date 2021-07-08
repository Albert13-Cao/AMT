#1. read all lines into a dict. dict key = number, value = repetitionive times
with open("cavalryin.txt") as cavalryin:
    current_line = 0
    troops = 0
    cavalry_dict = {}

    for line in cavalryin:
        current_line += 1
        if current_line == 1:
            troops = int(line)
        else:
            try:
                cavalry_dict[int(line)] += 1
            except KeyError:
                cavalry_dict[int(line)] = 1

#2. loop this dict, divided key / value, if all remainder == 0, then it is YES, else No.
result = "YES"
for key, value in cavalry_dict.items():
    if value % key != 0:
        result = "NO"
        break

#3. Save result into a output file 
with open("cavalryout.txt", "w") as cavalryout:
    cavalryout.write(result)