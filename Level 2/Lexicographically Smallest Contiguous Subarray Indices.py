def solution(l,t): 
    currentSum=l[0]
    startIndex=0
    n=len(l)
    for i in range(n+1):
        while currentSum>t and start<i-1:
            currentSum-=l[start]
            start+=1
        if currentSum==t:
            return [start,i-1]
        if i<n:
            currentSum+=l[i]
    return [-1,-1]