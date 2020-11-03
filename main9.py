class Student:
    def __init__(self,sno,name):
        self.sno = sno
        self.name = name

    def printstu(self):
        print(self.sno, self.name)


obj1 = Student(34,"Rahul")
obj2 = Student(56, "Ravinder")

obj1.printstu()
obj2.printstu()

print(type(obj1))