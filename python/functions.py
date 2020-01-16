#functions 
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

#variable number of arguments , like in print function
def var_args(name, *args):
    print(name)
    print(args)

#kwargs works like a dictionary
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"])

get_students_titlecase()
# add_student("mark",331)
# get_students_titlecase()
# var_args("Mark","loves Pyhton",None,"Hello",5)

# var_kwargs("Mark",description="loves Pyhton",feedback=None,pluralsight_subscriber=True)

#input function
student_name=input("Enter student name:")
student_id=input("Enter student id:")
add_student(student_name,student_id)
get_students_titlecase()

#yield functions - returneaza cate o linie din fisier de fiecare data cand e chemata , in loc de return e yield

#lambda functions- functions that don't have a name or keyword def to define them, are short, one line of code
# def double(x):
#     return x*2

double=lambda x: x*2

print(double(5))


 