def fun(num):
    length=len(str(num))
    rev=0
    for i in range(length):
        
        last=num%10
        rev=rev*10+last
        num=num//10
    print(rev)

num=int(input("Enter a number : "))
fun(num)