with open("farmin.txt") as filein:
    lines = filein.readlines()
    spaces = int(lines[0])
    space_list = lines[1].strip().split(" ")
    # print(spaces, space_list)

left_index = 0
right_index = spaces - 1
cuts = 0
left_sum = int(space_list[0])
right_sum = int(space_list[spaces - 1])
while right_index > left_index:
    if left_sum == right_sum:
        left_index += 1
        right_index -= 1
        left_sum = int(space_list[left_index])
        right_sum = int(space_list[right_index])
    elif left_sum > right_sum:
        right_index -= 1
        right_sum += int(space_list[right_index])
        cuts += 1
    elif left_sum < right_sum:
        left_index += 1
        left_sum += int(space_list[left_index])
        cuts += 1

print(cuts)

with open("farmout.txt", "w") as fileout:
    fileout.write(str(cuts))