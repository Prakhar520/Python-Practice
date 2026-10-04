num=int(input("enter a number:"))
factorial=(num+1)
counter=num

while counter<=num:
    factorial *= counter
    counter += num

print("factorial",num,"is:",factorial)