with open("listin.txt") as listin:
    #1. read all information to a dict, containing person and its friend amount
    current_line = 0
    friend_people_number = 0
    friend_dict = {}
    max_friends = 0
    best_players = []
    
    for line in listin:
        current_line += 1

        if current_line == 1:
            friend_people_number = int(line)
            # print(type(friend_people_number))
        else:
            line = line.strip()
            friend_pair = line.split()
            # print(friend_pair)
            if friend_pair[0] in friend_dict.keys():
                friend_dict[friend_pair[0]] += 1
            else:
                friend_dict[friend_pair[0]] = 1
            
            if friend_pair[1] in friend_dict.keys():
                friend_dict[friend_pair[1]] += 1
            else:
                friend_dict[friend_pair[1]] = 1

            if friend_dict[friend_pair[0]] > max_friends:
                max_friends = friend_dict[friend_pair[0]] 
                best_players = [int(friend_pair[0])]
            elif friend_dict[friend_pair[0]] == max_friends:
                best_players.append(int(friend_pair[0]))
    
            if friend_dict[friend_pair[1]] > max_friends:
                max_friends = friend_dict[friend_pair[1]] 
                best_players = [int(friend_pair[1])]
            elif friend_dict[friend_pair[1]] == max_friends:
                best_players.append(int(friend_pair[1]))
    
    print(best_players)
    best_players.sort() 
    print(best_players)

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