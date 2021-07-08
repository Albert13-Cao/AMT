#1.read the file into a list
with open("cloudin.txt") as cloudin:
    current_line = 0
    max_length = 1000000000
    temp_sum = 0
    
    temp_list = cloudin.readlines()

    #2. loop the list 
    #2.1 read item1, get number of people and people to cover
    #2.2 go through the rest, add "people to cover" items into a sum .
    #2.3 when current line > "people to cover", subtract the first item from sum
    #2.4 when sum < max, set max = sum
    for value in temp_list:
        if current_line == 0:
            infomation = temp_list[0].split(' ')
            number_of_people = int(infomation[0])
            people_to_cover = int(infomation[1])
        else:
            if current_line > number_of_people:
                break

            temp_sum += int(value)
            if current_line > people_to_cover:
                temp_sum -= int(temp_list[current_line - people_to_cover])
            
            if current_line >= people_to_cover:
                if temp_sum < max_length:
                    max_length = temp_sum
        
        current_line += 1

#3. Save into output file
with open("cloudout.txt", "w") as cloudout:
    cloudout.write(str(max_length))