#1. read all the information from txt file 

with open("baublesin.txt") as baublesin:
    line = baublesin.readlines()
    # print(line)
    nums = (line[0]).split()
    
    red = int(nums[0])
    blue = int(nums[1])
    spare = int(nums[2])
    target_red = int(nums[3])
    target_blue = int(nums[4])

    #2. there are 5 variables : red, blue, spare, target red, target blud
    # make 3 calcuations 
    # a. red + spare - target red + 1
    # b. blue + spare - target blue + 1
    # c. red + blue + spare - (target red + target blue) + 1
    # finally, find minimal of a, b, and c.
    
    result_1 = red + spare - target_red + 1
    result_2 = blue + spare - target_blue + 1
    result_3 = red + blue + spare - (target_red + target_blue) + 1

    result = min(result_1, result_2, result_3)

    if result < 0:
        result = 0

    #3. save into output file
    with open("baublesout.txt", "w") as baublesout:
        baublesout.write(str(result))