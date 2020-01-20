#readable and reusable code, instead of dictionary
#doesn't have access modifiers, all are public , no override keyword, no interfaces

students=[]

#declare class
class Student:
    #pass                        #do nothing
    school_name="UPT"
    def __init__(self,name,student_id=332): #constructor
        self.name=name
        self.student_id=student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()
    
    def get_school_name(self):
        return self.school_name

#self, the way we refer at out class from inside the class , like 'this'

student=Student("Mark")
print(student)

#until now we used instance attributes, but we can have class attributes that is something every instance we want to have, outside of methods but inside the class

print(Student.school_name)

#inheritance

class HighSchoolStudent(Student):
    school_name="Springfield HighSchool"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalize(self):
        original_value=super().get_name_capitalize() #look in parent class
        return original_value + "-HS"


james=HighSchoolStudent("james")
print(james.get_name_capitalize())



