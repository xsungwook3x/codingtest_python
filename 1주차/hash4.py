from collections import defaultdict

def solution(genres, plays):

    album = defaultdict(list)
    num = []
    answer = []
    for i in range(len(genres)):
        album[genres[i]].append([plays[i],i])
        
    for key in album.keys():
        album[key].sort(key = lambda x: (-x[0],x[1]))
        
    for key,value in album.items():
        sum = 0
        
        for v in value:
            sum +=v[0]
            
        num.append([key,sum])
        
    num.sort(key = lambda x: -x[1])
    
    for genre,_ in num:
        
        if len(album[genre]) ==1:
            answer.append(album[genre][0][1])
            
        else:
            answer.append(album[genre][0][1])
            answer.append(album[genre][1][1])
            
    return answer