def cool(operation=None,a=1,b=2,c=3):
    if(operation==None):
        print("choose a known operation")
        return 0
    elif(operation=="sum"):
        print("Arguments values are a =",a,",b= ",b,",c=",c)
        sum=a+b+c
        print("Sum of arguments is :",sum)
        return sum
    elif(operation=="divide"):
        result=a/b
        print("we tried to divide ",a, "by",b,"and we got",result)
        return result
    elif(b==0):
         print('we  cant divide 0')
         return 0
    else:
        return 0

x=cool()
x+=cool("sum")
x+=cool("sum",2,2,2)
x+=cool("divide")
x+=cool("divide",3,3,3)
print(x)