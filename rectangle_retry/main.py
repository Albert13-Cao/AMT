with open("bendin.txt") as bendin:
    lines = [line.rstrip() for line in bendin]
    list1 = (lines[0]).split(" ")
    list2 = (lines[1]).split(" ")
    x1 = int(list1[0])
    y1 = int(list1[1])
    x2 = int(list1[2])
    y2 = int(list1[3])
    x11 = int(list2[0])
    y11 = int(list2[1])
    x12 = int(list2[2])
    y12 = int(list2[3])

    if x11 > x2 or y11 > y2 or x12 < x1 or y12 < y1:
        area1 = (x2 - x1) * (y2 - y1)
        area2 = (x12 - x11) * (y12 - y11)
        answer = area1 + area2
    else:
        bottom_left_x = x1
        if x11 > x1:
            bottom_left_x = x11
        bottom_left_y = y1
        if y11 > y1:
            bottom_left_y = y11
        top_right_x = x2
        if x12 < x2:
            top_right_x = x12
        top_right_y = y2
        if y12 < y2:
            top_right_y = y12

        overlap = (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y)
        # print(overlap)
        area1 = (x2 - x1) * (y2 - y1)
        # print(area1)
        area2 = (x12 - x11) * (y12 - y11)
        # print(area2)
        answer = area1 + area2 - overlap

    print(answer)

    with open("bendout.txt", "w") as bendout:
        bendout.write(str(answer))