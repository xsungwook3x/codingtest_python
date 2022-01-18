def solution(brown, yellow):
    total = brown + yellow
    ans = []


    for width in range(total,0,-1):
        if total % width != 0 : continue

        height =int(total/width)
        y = int((width - 2) * (height - 2))
        b = total - y 

        if y == yellow :
            if b == brown :
                ans.append(width)
                ans.append(height)
                break
        
    

    return ans;