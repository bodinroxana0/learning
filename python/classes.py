#readable and reusable code, instead of dictionary

students=[]

#declare class
class Student:
    #pass                        #do nothing
    def __init__(self,name,student_id=332): #constructor
        student={"name": name, "student_Id": student_id}
        students.append(student)

    def __str__(self):
        return "Student"

#self, the way we refer at out class from inside the class , like 'this'

student=Student("Mark")
print(student)