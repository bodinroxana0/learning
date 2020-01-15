def divide(a=2,b=2):
    if((a==0) & (b==0)):
         print('we  cant divide 0')
         return 0
    elif((a==0) & (b!=0)):
        result=a/b
        print("we tried to divide ",a, "by",b,"and we got",result)
        return result
    else:
        result=a/b
        print("we tried to divide ",a, "by",b,"and we got",result)
        return result
sum=divide(1,1)
sum+=divide()
sum+=divide(5)
sum+=divide(0)
sum+=divide(0,0)
print(sum)
