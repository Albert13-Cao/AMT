with open("tagin.txt") as tagin:
    current_line = 1
    # list_red = ["1"]
    # list_blue = ["2"]
    list_red = set("1")
    list_blue = set("2")
    for line in tagin:
        if current_line == 1:
            info = line.split(" ")
            people_playing = int(info[0])
            people_tagged = int(info[1])
        else:
            tag_info = line.split(" ")
            tagger = tag_info[0]
            tagged = tag_info[1].strip()
                
            # if tagger in list_red:
            #     try:
            #         list_red.add(tagged)
            #     except:
            #         pass
            # else:
            #     try:
            #         list_blue.add(tagged)
            #     except:
            #         pass
                
            if tagger in list_red:
                list_red.add(tagged)
            else:
                list_blue.add(tagged)
            # if tagger in list_red:
            #     list_red.append(tagged)
            # else:
            #     list_blue.append(tagged)
        
        current_line += 1
        
print(len(list_red), len(list_blue))

with open("tagout.txt", "w") as tagout:
    tagout.write(str(len(list_red)) + " " + str(len(list_blue)))