def re(n):
    rev=0
    while(n):
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
if(n==re(n)):
    print(n)
else:
    i=1
    while True:
        if(n+i == re(n+i)):
            print(n+i)
            break
        i+=1
