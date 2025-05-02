# 8 Write a python program to calculate N!

num = int(input("Enter num to Find Factorial = "))

def fact(n):
    if n==0 or n==1:
        return 1
    elif n>0:
        return n*fact(n-1)
    else:
        print("We cannot find Factorial of Negative num")

print(f"{num}! = {fact(num)}")