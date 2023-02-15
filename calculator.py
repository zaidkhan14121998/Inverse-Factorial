num1=int(input("enter a first number= "))
op=(input("enter operator"))
num2=int(input("enter a second number= "))

if op == "+":
    print(int(num1+num2))
elif op == "-":
    print(int(num1-num2))
elif op == "*":
    print(int(num1*num2))
elif op == "/":
    print(int(num1/num2))
else:
    print("invalid operator")



