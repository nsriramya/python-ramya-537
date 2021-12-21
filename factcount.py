from math import sqrt
def pr(n):
    f=2
    if(n==1):
        return 1
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            f+=2
        if(i*i==n):
            f-=1
    return f
n=int(input())
print(pr(n))
