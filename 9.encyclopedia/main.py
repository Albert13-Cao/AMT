with open("encyin.txt") as encyin:
    lines = [line.rstrip() for line in encyin]
    # print(lines)
    info = lines[0].split(' ')
    # print(info)
    n_of_pages = int(info[0])
    # print(n_of_pages)
    n_of_questions = int(info[1])
    pages_words_list = lines[1:(n_of_pages + 1)]
    # print(pages_words_list)
    # lines.remove(lines[:n_of_pages + 1])
    requests = lines[n_of_pages + 1:]
    answer = ""

    for i in range(n_of_questions):
        index = requests[i]
        answer_to_question = pages_words_list[int(index)-1]
        answer += str(answer_to_question)
        if int(i) == n_of_questions-1:
            break
        else:
            answer += "\n"

    with open("encyout.txt", "w") as encyout:
        encyout.write(answer)