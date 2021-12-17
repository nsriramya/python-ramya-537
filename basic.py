class Student:
    school="aditya"
    def __init__(self,m1,m2,m3):
        self.m1=10
        self.m2=20
        self.m3=30
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.school
        
s1=Student(10,20,20)
s2=Student(30,20,20)
 
print(s1.avg())
print(Student.info())
