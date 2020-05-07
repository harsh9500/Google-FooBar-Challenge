def solution(l):
    # Your code here
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

l=[1,2,3,4,5,6]
l=[1,1,1]
l=[2,3,5]
l=[1,5,6]
l=range(1,2001)
print(solution(l))