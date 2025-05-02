# 6 Write a Python program to find sum of n natural numbers without loop.
num= int(input("Enter the num = "))
def sum(n):
    if n>0:return n+sum(n-1)
   
print("The Sum of ",num," is = ",sum(num))

