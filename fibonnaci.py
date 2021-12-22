def fib(n):
    a=0
    b=1
    if(n==1):
        print(a,end="")

    else:
        print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
     
n=int(input())
fib(n)
