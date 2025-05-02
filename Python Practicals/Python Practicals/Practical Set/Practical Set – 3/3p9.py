# Write a python program to check whether given number is Armstrong or not.

num = int(input("Enter Number = "))
temp=num

def arm(n):
    rem=0
    sum=0
    
    while n>=1:
        rem=n%10
        sum+=rem*rem*rem
        n=n//10

    if temp==sum:
        print("The Num is Armstrong number")
    else:
        print("The Num is Not ___ Armstrong number")

arm(num)