def fun(num):
    n=1
    i=0
    while n<num:
        i+=1
        n*=i

    # inverse factorial we have but expect 23 also 4 its wronge 

    x=1
    for j in range(1,i+1):
        x*=j
        
    #now compare with org factorial and find factorial

    if num==x:
        print(i)
    else:
        print(f"{num} its not a factorial of any number")
    
num=int(input("enter a number : "))
fun(num)
