num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
opera=input("+,-,*,/: ")

if opera== '+':
    print("",num1+num2)

elif opera=='-':
    print("",num1-num2)

elif opera=='*':
    print("",num1*num2)

elif opera=='/':
    print("",num1/num2)

else:
    print("Invalid operator")