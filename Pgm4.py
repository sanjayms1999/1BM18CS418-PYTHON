class student:
    def __init__(self):
        self.__sid=None
        self.__age=None
        self.__marks=None
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            print("Enter Valid marks")
            return False
    def validate_age(self):
        if self.age>0:
            return True
        else:
            print("Enter Valid age")
            return False
    def check_qualification(self):
        if self.marks>=65 and self.age>20:
            print("Eligible")
        else:
            print("Not Eligible")
    def setter(self):
        self.sid=int(input("Enter sid "))
        self.age=int(input("Enter age " ))
        self.marks=int(input("Enter marks "))
 
    def getter(self):
        print("Student Details are")
        print("Sid : ",self.sid)
        print("Age : ", self.age)
        print("Marks : ",self.marks)
 
p=student()   
p.setter()
p.validate_marks()
p.validate_age()
p.check_qualification()
p.getter()
