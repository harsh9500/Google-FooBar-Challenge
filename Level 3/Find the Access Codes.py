def solution(l):
    answer=0
    listLength=len(l)
    while listLength>=2:
        listLength-=1
        currentEle=l[listLength]
        sum1,sum2=0,0
        for i in l[:listLength]:
            if currentEle % i==0:
                sum1+=1
        for j in l[listLength+1:]:
            if j % currentEle==0:
                sum2+=1
        answer+=(sum1*sum2)
    return answer