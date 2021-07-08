with open("dictin.txt") as dictin:
    # with open("file.txt") as file_in:
    # lines = dictin.readlines()
    # print(lines)
    line_num = 0
    dict_amount = 0
    to_translate = 0
    number_dict = {}
    for line in dictin:
        line_num += 1
        if line_num == 1:
            line = line.strip()
            temp_list = line.split(' ')
            dict_amount = int(temp_list[0])
            to_translate = int(temp_list[1])
            # print(dict_amount, to_translate)
        elif line_num <= dict_amount + 1:
            line = line.strip()
            temp_list = line.split(' ')
            integer_part = int(temp_list[0])
            number_part = int(temp_list[1])
            number_dict[integer_part] = number_part
        else:
            # answer = ""
            try:
                line = line.strip()
                value = str(number_dict[int(line)])
            except KeyError:
                value = "C?"
            print(value)

            with open("dictout.txt", "a") as dictout:
                if line_num != dict_amount + to_translate + 1:
                    dictout.write(value + "\n")
                else:
                    dictout.write(value)
            

    # print(number_dict)