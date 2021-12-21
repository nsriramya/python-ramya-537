from math import sqrt
def pr(n):
    f=2
    if(n==1):
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if(n%i==0):
            return False
    return True


n=int(input())
if(pr(n)):
    print("p")
else:
    print("np")
