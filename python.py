print("simple calculator")
print("select a number: ")
print("1.addition")
print("2.substration")
print("3.multiflication")
print("4.division")
perform=int(input("enter the 1/2/3/4: "))
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number:  "))
if perform==1:
    sum=num1+num2
    print("the addition of two number is: ",sum)
elif perform==2:
    sub=num1-num2
    print("the substraction of two number is: ",sub)
elif perform==3:
    mul=num1*num2
    print("the multiflication of two number is: ",mul)
elif perform==4:
    div=num1/num2
    print("the division of two number is: ",div)
else:
    print("try again later")
    system.exit()