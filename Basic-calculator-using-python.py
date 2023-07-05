
#Basic calculator using python

no1 = input("Enter first number : ")
no2 = input("Enter second number : ")


op = input("Choose operation - add /sub /mul /div : ")

if op == "add":
    print(int(no1) + int(no2))

if op == "sub":
    print(int(no1) - int(no2))

if op == "mul":
    print(int(no1) * int(no2))

if op == "div":
    print(int(no1) / int(no2))
