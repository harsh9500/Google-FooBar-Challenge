sqrt2=4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
exp=10**100
def power(n):
    return (sqrt2*n)//exp

def recur(n):
    if n==1:
        return 1
    if n<1:
        return 0
    return n*power(n)+n*(n+1)/2-power(n)*(power(n)+1)/2-recur(power(n))

def solution(s):
    s=long(s)
    return str(recur(s))