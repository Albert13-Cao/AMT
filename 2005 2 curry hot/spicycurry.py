with open("curryin.txt") as filein:
    food = filein.readline().split()
    curry = int(food[0])
    rice = int(food[1])
    veggies = int(food[2])
    

x = 0
y = 0
z = 0
while True:
    if curry <= rice and curry <= veggies:
        x += 1
        rice -= 1
        veggies -= 1
    elif rice <= curry and rice <= veggies:
        y += 1
        curry -= 1
        veggies -= 1
    else:
        z += 1
        rice -= 1
        curry -= 1

    if ((curry == 0 and rice == 0) or (curry == 0 and veggies == 0) or (veggies == 0 and rice == 0)):
        break
# print(x, y, z)

with open("curryout.txt", "w") as fileout:
    fileout.write(str(x) + " " + str(y) + " " + str(z))