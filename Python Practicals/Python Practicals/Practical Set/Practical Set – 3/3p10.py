# Write a python program to check whether given number is Palindrome or not.

num = int(input("Enter Number = "))
temp=num

def palindrome(n):
    rem=0
    rev=0
    
    while n>=1:
        rem=n%10
        rev=rev*10+rem
        n=n//10

    if temp==rev:
        print("The Num is Palindrome number")
    else:
        print("The Num is Not ___ Palindrome number")

palindrome(num)