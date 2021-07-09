with open("manin.txt") as manin:
    mango_location = 0
    #1. get infomation: ishraq's location, celement's location, ishraq's distanse to mango, celement's distance to mango
    line_list = manin.readlines()
    print(line_list)
    infomation = line_list[0].split(" ")
    i_location = int(infomation[0])
    c_location = int(infomation[1])
    i_distance = int(infomation[2])
    c_distance = int(infomation[3])

#2. do the logic:
# absolute value of ishraq's location - mango's location = ishraq's distance to mango 
# absolute value of celement's location - mango's location = celement's distance to mango 
mango_location = i_location + i_distance
if abs(mango_location - c_location) == c_distance:
    pass
else:
    mango_location = -1 * i_distance + i_location
    if abs(mango_location - c_location) != c_distance:
        #unlikely to happen
        print("Something wrong happened")

print(mango_location)

with open("manout.txt", "w") as manin:
    manin.write(str(mango_location))