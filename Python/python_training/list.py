def func1(list_ex):
    list_ex.pop(0)

list1=[1,2,3]
list2=[]
list2=list1
print(id(list1))
print(id(list2))

func1(list1)
print(list1)