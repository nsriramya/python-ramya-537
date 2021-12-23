def insert_end(val):
    nn=Node(val)
    if head==None:
        head=nn
    else:
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=nn
        
        
        
        
        
        
        
        
