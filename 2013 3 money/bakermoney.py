with open("savein.txt") as filein:
    temp_list = filein.readlines()
    num_of_ingredients = temp_list[0]
    min_cost = 0
    total = 0

    three_list = []
    four_list = []

    for i in range(1, len(temp_list)):
        item = int(temp_list[i])
        item_rounded = item
        if item % 5 < 3:
            if item % 5 == 1:
                item_rounded = item - 1
            elif item % 5 == 2:
                item_rounded = item - 2
            total += item_rounded
        elif item % 5 == 3:
            three_list.append(item)
        else:
            four_list.append(item)

    #treat 3-list and 4-list. Logic is: combine one from 4-list and one from 3-list.
    #if 4-list has more items, then group them in 3 items, then add the remaining and round
    #if 3-list has more items, then group them in 2 items, then add the remaining and round
    three_length = len(three_list)
    four_length = len(four_list)
    if three_length == four_length:
        for i in range(three_length):
            temp_sum = three_list[i] + four_list[i]
            total += temp_sum - 2
    elif three_length > four_length:
        for i in range(three_length):
            if i < four_length:
                temp_sum = three_list[i] + four_list[i]
                total += temp_sum - 2
            else:
                total += three_list[i]
            
        total -= ((three_length - four_length) // 2) * 1
        total += ((three_length - four_length) % 2) * 2
    else:
        for i in range(four_length):
            if i < three_length:
                temp_sum = three_list[i] + four_list[i]
                total += temp_sum - 2
            else:
                total += four_list[i]
            
        total -= ((four_length - three_length) // 3) * 2
        total += ((four_length - three_length) % 3) * 1
    
with open("saveout.txt", "w") as fileout:
    fileout.write(str(total))