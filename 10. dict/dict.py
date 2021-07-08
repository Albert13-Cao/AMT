with open("dictin.txt") as dictin:
    num_dict = {}
    to_translate = 0
    dict_words = 0
    num_questions = 0

    current_line = 0
    for line in dictin:
        current_line += 1
        # print(type(line))
        if current_line == 1:
            info = line.split()
            dict_words = int(info[0])
            num_questions = int(info[1])
            # print(dict_words, num_questions)
        elif current_line <= dict_words + 1 :
            info = line.split()
            # print(info)
            num_dict[info[0]] = info[1]
            # print(num_dict)
        else:
            # print(line)
            try:
                line = line.strip()
                # print(line, value)
                value = num_dict[line]
                # print(value)
            except:
                value = "C?"
                # print(value)
                
            with open("dictout.txt", "a") as dictout:
                if current_line != num_questions + dict_words + 1:
                    dictout.write(str(value) + "\n")
                else:
                    dictout.write(value)