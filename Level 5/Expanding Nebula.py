prevMap={
    ((0,0),(0,0)):0,
    ((0,0),(0,1)):1,
    ((0,0),(1,0)):1,
    ((0,0),(1,1)):0,
    ((0,1),(0,0)):1,
    ((0,1),(0,1)):0,
    ((0,1),(1,0)):0,
    ((0,1),(1,1)):0,
    ((1,0),(0,0)):1,
    ((1,0),(0,1)):0,
    ((1,0),(1,0)):0,
    ((1,0),(1,1)):0,
    ((1,1),(0,0)):0,
    ((1,1),(0,1)):0,
    ((1,1),(1,0)):0,
    ((1,1),(1,1)):0
    }
curMap={
    0:(
     ((0,0),(0,0)),
     ((0,0),(1,1)),
     ((0,1),(0,1)),
     ((0,1),(1,0)),
     ((0,1),(1,1)),
     ((1,0),(0,1)),
     ((1,0),(1,0)),
     ((1,0),(1,1)),
     ((1,1),(0,0)),
     ((1,1),(0,1)),
     ((1,1),(1,0)),
     ((1,1),(1,1))
        ),
    1:(
        ((1,0),(0,0)),
        ((0,1),(0,0)),
        ((0,0),(1,0)),
        ((0,0),(0,1))
        )
    }

def transpose(matrix):
    return tuple(zip(*matrix))

def generateCol(first,column):
    botrows=(
        (0,0),
        (0,1),
        (1,0),
        (1,1)
        )
    possibilities=[]
    for key in first:
        choices=[]
        for row in botrows:
            if prevMap[((key[0],key[1]),row)]==column[0]:
                choices.append(row)
        for n in range(1,len(column)):
            next=[]
            if choices is None:
                return
            for col in choices:
                for m in range(2):
                    temp=list(col)
                    if prevMap[((key[n],key[n+1]),(col[n],m))]==column[n]:
                        temp.append(m)
                        next.append(temp)
            choices=next
        [possibilities.append((key,tuple(choice))) for choice in choices]
    return tuple(possibilities)

def generateFirstCol(col):
    botrows=(
        (0,0),
        (0,1),
        (1,0),
        (1,1)
        )
    choices=curMap[col[0]]
    for idx in range(1,len(col)):
        columns=[]
        for prev in choices:
            for botrow in botrows:
                if prevMap[(prev[idx],botrow)]==col[idx]:
                    columns.append(prev[:]+(botrow,))
        choices=tuple(columns)
    return tuple([transpose(sol) for sol in choices])

def solution(g):
    # Your code here
    for row in range(len(g)):
        for col in range(len(g[0])):
            g[row][col]=int(g[row][col])
            
    rotation=transpose(g)
    first={}
    validPreImages=generateFirstCol(rotation[0])
    for preimage in validPreImages:
        if preimage[1] not in first:
            first[preimage[1]]=1
        else:
            first[preimage[1]]+=1
    
    for n in range(1,len(rotation)):
        second={}
        validPreImages=generateCol(first,rotation[n])
        for preimage in validPreImages:
            if preimage[0] in first:
                if preimage[1] in second:
                    second[preimage[1]]+=first[preimage[0]]
                else:
                    second[preimage[1]]=first[preimage[0]]
            else:
                pass
        first=second
        
    return sum(first.values())