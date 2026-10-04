temp=int(input("enter the temperature:"))
unit=input("enter the unit(c or f): ")


if unit=="c":
    convertion=temp*9/5+32
    print("here is ur convwerted unit to farenheit: ",convertion)

elif unit=="f":
    convertion=(temp-32)*5/9
    print("here is ur converted unit to celsius: ",convertion)

else:
    print("wrong input")