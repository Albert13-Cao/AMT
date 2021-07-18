with open("hippoin.txt") as filein:
    line = filein.readlines()
    flower_number = int(line[0])
    hippo_1 = int(line[1])
    hippo_2 = int(line[2])
    hippo_3 = int(line[3])
    # print(flower_number, hippo_1, hippo_2, hippo_3)
    
    flowers_before = hippo_1 - 1
    # center_flowers = 0
    result = 0
    flowers_after = flower_number - hippo_3
    flowers_between_1_2 = hippo_2 - hippo_1 - 1
    flowers_between_2_3 = hippo_3 - hippo_2 - 1

    flowers_inbetween = max(flowers_between_1_2, flowers_between_2_3)
    if flowers_inbetween >= flowers_before or flowers_inbetween >= flowers_after:
        result = flowers_inbetween + max(flowers_before, flowers_after)
    else:
        result = flowers_before + flowers_after
        
    
with open("hippoout.txt", "w") as fileout:
    fileout.write(str(result))