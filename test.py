a=int(input("enter the number : "))
b=int(input("enter the number : "))
choice=int(input("enter the choice(+,-,*,/) : "))
if choice==1:
    print("the sum is : ",a+b)
elif choice==2:
    print("the difference is : ",a-b)
elif choice==3:
    print("the product is : ",a*b)
elif choice==4:
    print("the quotient is : ",a/b)
else:
    print("invalid choice")