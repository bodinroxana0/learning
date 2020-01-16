
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

def save_file(student):
    try:
        f=open("students.txt","a") #access mode w-writing,overwrites the entire file; r-reading; a-appending to a new or existing file; rb-reading binary file; wb-writing binary
        f.write(student+ "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f=open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

read_file()
get_students_titlecase()

student_name=input("Enter student name:")
student_id=input("Enter student id:")
add_student(student_name,student_id)

save_file(student_name)