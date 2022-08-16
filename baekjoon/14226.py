from collections import deque
a=int(input())


queue=deque()
queue.append([1,0,0])
visited=[[False]*1001 for _ in range(1001)]
visited[1][0]=True

while queue:
    curr,clip,t=queue.popleft()

    if curr==a:
        print(t)
        break

    for i in range(3):  # 연산을 3번 수행한다.


        if i == 0:
            new_clipboard, new_screen = curr, curr


        elif i == 1:
            new_screen, new_clipboard = curr + clip, clip

        else:
            new_screen, new_clipboard = curr - 1, clip


        if new_screen >= 1001 or new_screen < 0 or new_clipboard >= 1001 or new_clipboard < 0 or visited[new_screen][new_clipboard]:
            continue

        visited[new_screen][new_clipboard] = True
        queue.append([new_screen, new_clipboard, t + 1])
