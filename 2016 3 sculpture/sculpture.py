with open("artin.txt") as filein:
    current_line = 0
    blocks = 0
    max_height = 0
    current_blocks = []
    current_time = 0

    for line in filein:
        current_line += 1
        if current_line == 1:
            blocks = int(line)
            continue

        line = line.strip()
        temp_list = line.split(" ")
        second_after = int(temp_list[0])
        width = int(temp_list[1])
        height = int(temp_list[2])

        #shift right
        shift = second_after - current_time
        current_time = second_after
        i = 0
        while i < shift and len(current_blocks) > 0:
            current_blocks.pop()
            i += 1
        
        i = 0
        while i < width:
            try:
                current_blocks[i] += height
                if current_blocks[i] > max_height:
                    max_height = current_blocks[i]
            except IndexError:
                current_blocks.append(height)

            i += 1

# print(max_height)
with open("artout.txt", "w") as fileout:
    fileout.write(str(max_height))

    