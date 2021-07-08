with open("bendin.txt") as bendin:
    lines = [line.rstrip() for line in bendin]
    # print(lines)
    nums1 = lines[0]
    nums2 = lines[1]
    list1 = nums1.split(" ")

    list2 = nums2.split(" ")
    x1 = int(list1[0])
    y1 = int(list1[1])
    x2 = int(list1[2])
    y2 = int(list1[3])
    x11 = int(list2[0])
    y11 = int(list2[1])
    x12 = int(list2[2])
    y12 = int(list2[3])

    if x12 <= x1 or y12 <= y1 \
        or x11 >= x2 or y11 >= y2:
        ## not overlapped
        area1 = (x2 - x1) * (y2 - y1)
        area2 = (x12 - x11) * (y12 - y11)
        answer = area1 + area2
    else:
        bottom_left_x = x1
        if x1 < x11 :
            bottom_left_x = x11

        bottom_left_y = y1
        if y1 < y11:
            bottom_left_y = y11

        top_right_x = x2
        if x2 > x12:
            top_right_x = x12

        top_right_y = y2
        if y2 > y12:
            top_right_y = y12

        overlap = (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y)
        area1 = (x2 - x1) * (y2 - y1)
        area2 = (x12 - x11) * (y12 - y11)
        # print(bottom_left_x, bottom_left_y, top_right_x, top_right_y)
        # print(overlap, area1, area2)
        answer = area1 + area2 - overlap

    print(answer)

    with open("bendout.txt", "w") as bendout :
        bendout.write(str(answer))