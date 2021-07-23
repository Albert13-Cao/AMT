with open("chairsin.txt") as filein:
    lines = filein.readlines()
    temp_list = lines[0].strip().split(" ")
    people_amount = int(temp_list[1])
    wet_allowed = int(temp_list[2])
    chairs = lines[1]
    # print(people_amount, wet_allowed)

    current_queue = []
    current_index = 0
    wet_chair = 0
    people = 0
    while people < people_amount:
        current_queue.append(chairs[current_index])
        if chairs[current_index] == 'w':
            wet_chair += 1
            if wet_chair <= wet_allowed:
                people += 1
        else:
            people += 1

        current_index += 1

    print(current_queue)
    print(current_index)
    min_span = len(current_queue)
    while True:
        poped = current_queue.pop()
        
