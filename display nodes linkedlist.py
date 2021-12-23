class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
s1=Node(3)
s2=Node(4)
s3=Node(5)
if(s1==None):
    print("nonodes")
else:
    temp=s1
    while temp:
        print(temp.val)
        temp=temp.next
