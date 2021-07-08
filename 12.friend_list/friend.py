with open("listin.txt") as listin:
    #1. read all information to a dict, containing person and its friend amount
    current_line = 0
    friend_people_number = 0
    friend_dict = {}

    for line in listin:
        current_line += 1

        if current_line == 1:
            friend_people_number = int(line)
            # print(type(friend_people_number))
        else:
            line = line.strip()
            friend_pair = line.split()
            # print(friend_pair)
            try:
                friend_dict[friend_pair[0]] += 1
            except:
                friend_dict[friend_pair[0]] = 1

            try:
                friend_dict[friend_pair[1]] += 1
            except:
                friend_dict[friend_pair[1]] = 1
            # if friend_pair[0] in friend_dict.keys():
            #     friend_dict[friend_pair[0]] += 1
            # else:
            #     friend_dict[friend_pair[0]] = 1
            
            # if friend_pair[1] in friend_dict.keys():
            #     friend_dict[friend_pair[1]] += 1
            # else:
            #     friend_dict[friend_pair[1]] = 1
    
    #2 loop this dict, find persons with maximum friend amount, save the result into a list
    max_friends = 0
    best_players = []
    for person in friend_dict:
        if friend_dict[person] > max_friends:
            max_friends = friend_dict[person]
            best_players = [int(person)]
        elif friend_dict[person] == max_friends:
            best_players.append(int(person))

    best_players.sort()

    #3 convert this list to a string with \n and save it to the output file
    result = ""
    current_line = 0
    for person in best_players:
        current_line += 1
        if current_line == len(best_players):
            result += str(person)
        else:
            result += str(person) + "\n"    
        
    with open("listout.txt", "w") as listout:
        listout.write(result)