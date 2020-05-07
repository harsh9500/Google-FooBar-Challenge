from fractions import Fraction, gcd
import unittest

def multiplyMatrices(a,b):
    aRows=len(a)
    aCols=len(a[0])
    bCols=len(b[0])
    c=[]
    for i in range(aRows):
        c+=[[0]*bCols]
    for row in range(aRows):
        for col in range(bCols):
            dotProduct=Fraction(0,1)
            for temp in range(aCols):
                dotProduct+=a[row][temp]*b[temp][col]
            c[row][col]=dotProduct
    return c

def getSubMatrix(m,rows,cols):
    newMatrix=[]
    for i in rows:
        temp=[]
        for j in cols:
            temp.append(m[i][j])
        newMatrix.append(temp)
    return newMatrix

def identityMatrix(n):
    newMatrix=[]
    for i in range(n):
        newMatrix+=[[0]*n]
    for i in range(n):
        newMatrix[i][i]=Fraction(1,1)
    return newMatrix

def multiplyRowOfSquareMatrix(m,row,k):
    n=len(m)
    rowOperator=identityMatrix(n)
    rowOperator[row][row]=k
    return multiplyMatrices(rowOperator,m)

def addMultipleOfRowOfSquareMatrix(m,sourceRow,k,targetRow):
    n=len(m)
    rowOperator=identityMatrix(n)
    rowOperator[targetRow][sourceRow] = k
    return multiplyMatrices(rowOperator, m)

def invertMatrix(m):
    n=len(m)
    inverse=identityMatrix(n)
    for col in range(n):
        diagonalRow=col
        k=Fraction(1,m[diagonalRow][col])
        m=multiplyRowOfSquareMatrix(m,diagonalRow,k)
        inverse=multiplyRowOfSquareMatrix(inverse,diagonalRow,k)
        sourceRow=diagonalRow
        for targetRow in range(n):
            if sourceRow!=targetRow:
                k = -m[targetRow][col]
                m=addMultipleOfRowOfSquareMatrix(m,sourceRow,k,targetRow)
                inverse=addMultipleOfRowOfSquareMatrix(inverse,sourceRow, k, targetRow)
    return inverse

def lcm(a,b):
    result = a*b / gcd(a, b)
    return result
    
def lcmForArrays(args):
    arrayLength=len(args)
    if arrayLength<=2:
        return lcm(*args)

    initial=lcm(args[0], args[1])
    i=2
    while i<arrayLength:
        initial=lcm(initial, args[i])
        i+=1
    return initial

def solution(m):
    # Your code here
    terminalStates=[]
    nonTerminalStates=[]
    for i, row in enumerate(m):
        if sum(row)==0:
            terminalStates.append(i)
        else:
            nonTerminalStates.append(i)
    if len(terminalStates)==1:
        return [1,1]
    
    for i,row in enumerate(m):
        rowSum=sum(m[i])
        if rowSum==0:
            m[i][i]=1
        else:
            for j, column in enumerate(row):
                # print(j,column)
                m[i][j]=Fraction(column,rowSum)
    print(m)

    q=getSubMatrix(m,nonTerminalStates,nonTerminalStates)
    r=getSubMatrix(m,nonTerminalStates,terminalStates)
    print(q)
    print(r)
    idMatrix=identityMatrix(len(q))
    iMinusq=[]
    for i,row in enumerate(idMatrix):
        temp=[]
        for j, column in enumerate(row):
            temp.append(idMatrix[i][j]-q[i][j])
        iMinusq.append(temp)
    
    result=multiplyMatrices(invertMatrix(iMinusq),r)
    denominator=lcmForArrays([item.denominator for item in result[0]])
    result=[item.numerator*denominator / item.denominator for item in result[0]]
    result.append(denominator)
    return result


    
test_input = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(solution(test_input))