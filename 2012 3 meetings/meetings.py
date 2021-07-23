with open("arthin.txt") as filein:
    duel_knight_num = 0
    current_line = 1
    knights_found = ['']
    for line in filein:
        if current_line == 1:
            knight_num = int(line)
        elif current_line == 2:
            prone_knights = int(line)
        else:
            