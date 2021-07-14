with open("snapin.txt") as filein:
    line = filein.readline()
    temp_list = line.split(" ")
    # row = int(temp_list[0])
    # col = int(temp_list[1])
    rr = int(temp_list[2])
    rc = int(temp_list[3])
    sr = int(temp_list[4])
    sc = int(temp_list[5])
    
    with open("snapout.txt", "w") as fileout:
        if ((rr - rc) + (sr - sc)) % 2 == 0:
            fileout.write("SCARLET")
        else:
            fileout.write("ROSE")