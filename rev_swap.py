'''
9
1 9 2 8 3 7 4 6 5
'''
n=int(input())
d=list(map(int,input().split()))
f=d.sort(reverse=True)
if(n%2!=0):
    n=n-1
    for i in range(0,n,2):
        d[i],d[i+1]=d[i+1],d[i]
    print(*d)
