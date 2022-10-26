board=[list(map(int,input().split())) for _ in range(9)]
blank=[]
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            blank.append([i,j])

def checkRow(x,a):
    for i in range(9):
        if board[x][i]==a:
            return False
    return True

def checkColumn(y,a):
    for i in range(9):
        if board[i][y]==a:
            return False
    return True

def checkBox(x,y,a):
    nx=x//3*3
    ny=y//3*3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx==len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkColumn(y, i) and checkBox(x, y, i):
            board[x][y] = i
            dfs(idx + 1)
            board[x][y] = 0

dfs(0)