class Que:
    def __init__(self,size,data=[]):
        self.size=size
        self.data=data
    def enqueue(self,val):
        if(len(self.data)==self.size):
            print("que is full")
        else:
            self.data.append(val)
    def dequeue(self):
        if len(self.data)==0:
            return "pop is not pos"
        return self.data.pop(0)
    
q1=Que(5,[1.2])
