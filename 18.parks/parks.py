#1.read all of the infomation from streetin.txt: number of buildings & parks and number of parks
with open("streetin.txt") as streetin:
    info = (streetin.readlines())[0]
    temp = info.split(" ")
    structures = int(temp[0])
    parks = int(temp[1])
    buildings = structures - parks

#2. caulculate the logic:
#  if number of parks is 1: (buildings & parks - parks) / 2
#  elif number of parks is 0: buildings & parks
#  elif buildings < parks: buildings
#  else:(buildings & parks - parks) / parks
answer = 0
if buildings % (parks + 1) == 0:
    answer = buildings // (parks + 1)
else: 
    answer = buildings // (parks + 1) + 1

# 3: save the answer in streetout.txt as a string
with open("streetout.txt", "w") as streetout:
    streetout.write(str(answer))