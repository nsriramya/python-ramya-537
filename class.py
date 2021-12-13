class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
s1=Student("ram",37)
s1.display();
