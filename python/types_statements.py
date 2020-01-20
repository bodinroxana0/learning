print("hello world")

name="python"
machine="HAL"
print("nice to meet you {0}. I am {1}".format(name,machine))
print(f"nice to meet you {name}. I am {machine}") #string interpolation

python=True
t=int(python)
print(t)

a=1
b=2
print("bigger" if a>b else "smaller") #ternary if

names=["Mark","Jessica","Homer"]
print(names[-1]) #print element at certain index
print("Mark" in names) #verify existence
print(len(names)) #length


print(names)
del names[1]
print(names)
names.append("Jessica")
print(names)

#list slicing
print(names[1:]) #skips first element
print(names[1:-1])

#loops
for name in names:
    print("Student name is {0}".format(name))

#for index in range(10) , created a list of 10 elements
#range can take up to 3 arg : range(5,10,2) where 5-start 10-stop 2-increment value

#break for stoping when finding the 1 we want
#continue when we want to ignore the 1 we want

#while loop - check condition before entering the loop
x=0
while x < 10:
    print("Count is {0}".format(x))
    x+=1   #manually increment the index

#dictionaries- ist with more detailes, key + value = pair , syntax like JSON 
student={
    "name":"Mark",
    "student_id": 15,
    "feedback": None
}
all_students=[
    {"name":"Mark","student_id": 15},
    {"name":"Jessica","student_id": 16}
]
print(student.keys())
print(student.values())
student["name"]="James"
print(student.values())

#exceptions - catch an eror and print a message but continue to run the code
student["last_name"]="Ana"

try:
    last_name=student["last_name"]
    numbered_last_name=3+last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("Error about the type")
    print(error) #to see exactly the error message
except Exception:
    print("Unkown error")
print("This code executes")
