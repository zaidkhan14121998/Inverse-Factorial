x=int(input("enter a number"))

for i in range(2,x//2+1):
    if x%i == 0:
        y=0
        break
    y=1
if y==0:
    print("not prime")

else:
    print("prime")

