#ask the user if they want to add a student or not , if they type yes you will add, and keep doing that until they type no. Then, print all the students from the list and exit
students=[]

def get_students_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase=student["name"].title()
        print(students_titlecase)

def add_student(name,student_id=332): #default value
    #define a dictionary
    student={"name": name, "student_Id": student_id}
    students.append(student)

answear=input("Do you want to add a new student?(Yes/No)")
while answear=="Yes":
    student_name=input("Enter student name:")
    student_id=input("Enter student id:")
    add_student(student_name,student_id)
    answear=input("Do you want to add a new student?(Yes/No)")

if answear=="No":
    get_students_titlecase()