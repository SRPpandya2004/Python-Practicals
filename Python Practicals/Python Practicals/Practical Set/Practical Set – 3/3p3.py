# 3 Write a Python program to find N factorial.

num=int(input("Enter Digit to find Factorial : "))

def fact(n):
    if n==0 or n==1:
        return 1
    elif n>0:
        return n*fact(n-1)
    else:
        print("FActorial does not exists for Nagative Num")

print("The factorial of ",num," is = ",fact(num) )