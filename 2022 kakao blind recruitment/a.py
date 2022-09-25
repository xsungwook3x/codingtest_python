def solution(commands):
    table = [["EMPTY"] * 10 for _ in range(10)]
    answer = []

    for command in commands:
        com_list = command.split(" ")
        if com_list[0] == "UPDATE":
            if len(com_list) == 4:
                if " " in table[int(com_list[1])][int(com_list[2])]:
                    a = table[int(com_list[1])][int(com_list[2])]
                    t_r, t_c = map(int, a.split(" "))
                    table[t_r][t_c] = com_list[3]
                else:
                    table[int(com_list[1])][int(com_list[2])] = com_list[3]
            elif len(com_list) == 3:
                for i in range(1, 10):
                    for j in range(1, 10):
                        if table[i][j] == com_list[1]:
                            table[i][j] = com_list[2]

        elif com_list[0] == "MERGE":
            com, r1, c1, r2, c2 = com_list
            r1 = int(r1)
            c1 = int(c1)
            r2 = int(r2)
            c2 = int(c2)
            tmp = table[r1][c1]
            table[r2][c2] = r1 + " " + c1

        elif com_list[0] == "UNMERGE":
            com, r, c = com_list
            r = int(r)
            c = int(c)

            if " " in table[r][c]:
                t_r, t_c = map(int, table[r][c].split(" "))
                tmp = table[t_r][t_c]
                a = table[r][c]
                table[t_r][t_c] = "EMPTY"
            else:
                tmp = table[r][c]
                table[r][c] = "EMPTY"
                a = r + " " + c
            for i in range(51):
                for j in range(51):
                    if table[i][j] == a:
                        table[i][j] = "EMPTY"
            table[r][c] = tmp

        elif com_list[0] == "PRINT":
            com, r, c = com_list
            r = int(r)
            c = int(c)
            answer.append(table[r][c])

    print(table)

    return answer