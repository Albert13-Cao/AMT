with open("streetin.txt") as filein:
    answer = 0
    info = filein.readline().split(" ")
    parks = int(info[1])
    structures = int(info[0])
    buildings = structures - parks

answer = buildings // (parks + 1)
remainder = buildings % (parks + 1)
if remainder > 0:
    answer += 1

with open("streetout.txt", "w+") as fileout:
    fileout.write(str(answer))