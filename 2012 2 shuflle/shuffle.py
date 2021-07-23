with open("shufflein.txt") as filein:
    info = filein.readlines()
    chair_set = set([int(i) for i in info[1].split()])
    people_list = [int(i) for i in info[2].split()]
    imp_info = info[0].split()
    num_of_spots = int(imp_info[0])
    num_of_seats = int(imp_info[1])
    # print(chair_list, people_list)
    # print(num_of_spots, num_of_seats)

    while True:
        back_people_list = people_list[:]
        removed = 0
        for idx, people in enumerate(people_list):
            if people in chair_set:
                print("Find people ", idx, people)
                back_people_list.pop(idx)
                removed += 1
                chair_set.remove(people)
            else:
                if back_people_list[idx - removed] + 1 > num_of_spots:
                    back_people_list[idx - removed] = 1
                else:
                    back_people_list[idx - removed] += 1
        
        if len(chair_set) == 0:
            break

        people_list = back_people_list[:]


    
                

            
            
        