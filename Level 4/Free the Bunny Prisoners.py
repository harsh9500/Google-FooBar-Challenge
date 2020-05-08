from itertools import combinations

def solution(num_buns, num_required):
    # Your code here
    answer=[[] for i in range(num_buns)]
    if num_required==0:
        return answer
    key=0
    combinationSize=num_buns-num_required+1
    for comb in combinations(answer,combinationSize):
        for tempComb in comb:
            tempComb.append(key)
        key+=1
    return answer