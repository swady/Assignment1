class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def printname(self):
        print(self.name,self.roll_number)

'''studentobj=Student("priyanka",118)
studentobj.printname()'''

class Student_child(Student):
    def __init__(self,name,roll_number):
        super().__init__(name,roll_number)

    def setAge(self,age):
        self.age=age

    def setMarks(self,marks1,marks2):
        self.marks=marks1
        self.marks=marks2

    def Display(self):
        print("Our Student name is and roll number is  ", self.name ,self.roll_number ,"and age is " , self.age ,"With the marks1 ",self.marks1 ,"and marks2 " ,self.marks2)

obj = Student_child("John",76,25,100,100)
obj.setAge()
obj.setMarks()
obj.Display()


    

        
    
