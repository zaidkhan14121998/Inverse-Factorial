
def fun(num):
    x=0
    y=1
    z=0
    while z<=num:
        print(z,end=" ")
        x=y
        y=z
        z=x+y
    
num=int(input("Enter a number : "))
fun(num)


