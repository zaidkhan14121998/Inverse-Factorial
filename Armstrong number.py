
print("Check Armstrong Number")

num=int(input("Enter a number"))

len=len(str(num))
sum=0
temp=num
while temp!=0:
        sum=sum+(temp%10) ** len
        temp=temp//10
if sum == num:
        print("this is armstrong number")
else:
        print("this is not armstrong number")
