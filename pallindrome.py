def ispa(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
    

n=int(input())
print(n==ispa(n))
