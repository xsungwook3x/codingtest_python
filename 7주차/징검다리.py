def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance) # [2,11,14,17,21,25]
    left = 0
    right = distance
    while left <= right:
        mid = (left + right)//2
        cnt = 0
        position = 0
        for i in range(len(sorted_rocks)):
            if sorted_rocks[i] - position < mid :
                cnt += 1
            else:
                position = sorted_rocks[i]
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer