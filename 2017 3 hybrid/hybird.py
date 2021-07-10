with open("chimin.txt") as filein:
    lines = filein.readlines()
    hybrid_length = int(lines[0])
    source_1 = lines[1].strip()
    source_2 = lines[2].strip()
    hybrid = lines[3].strip()

    # print(lines)

current_index = 0
slices = 0
result_str = "SUCCESS"
while current_index < hybrid_length:
    # print(hybrid[current_index])
    source1_index = current_index
    source2_index = current_index

    while source1_index < hybrid_length and hybrid[source1_index] == source_1[source1_index]:
        #source1 is promissing
        source1_index += 1

    while source2_index < hybrid_length and hybrid[source2_index] == source_2[source2_index]:
        #source1 is promissing
        source2_index += 1
             
    if source1_index == current_index and source2_index == current_index:
        result_str = "PLAN FOILED"
        break

    final_index = max(source1_index, source2_index)
    if final_index < hybrid_length:
        slices += 1
    steps = final_index - current_index
    # if steps == hybrid_length
    current_index += steps

print(slices, result_str)
with open("chimout.txt", "w") as fileout:
    if result_str == "SUCCESS":
        fileout.write(result_str + "\n" + str(slices))
    else:
        fileout.write(result_str)