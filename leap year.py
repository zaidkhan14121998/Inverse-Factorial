num=int(input("enter a number: "))

if num<0:
    print("Negative year is not exist in this universe ")
else:
    if num%4 == 0 and (num%400==0 or num%100 !=0):
        
        
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")



# def leap(x):
# 	if x%4==0 and x%100!=0:
# 		return 1
# 	elif x%4==0 and x%100==0 and x%400==0:
# 		return 1
# 	else:
# 		return 0
# x=int(input())
# print(leap(x))


#note :- 1 means leap year and 0 means not a leap year
    
    
    

    
