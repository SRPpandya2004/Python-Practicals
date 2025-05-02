# 2 WAP to find sum of N scanned numbers.

num = int(input("Enter element range of num = "))

sum=0

for x in range(0,num):

    temp=int(input(f"Enter num {x}= "))
    sum += temp
    
print(f"The sum of {num} elements =",sum)



#______________________________USing Rrcursion_____________________________________

def sum_of_numbers_recursive(n):
    # Base case: If n reaches 0, return 0
    if n == 0:
        return 0
    # Recursive case: sum of n numbers is the current number + sum of (n-1) numbers
    else:
        num = int(input("Enter a number: "))
        return num + sum_of_numbers_recursive(n - 1)

# Input number of elements
n = int(input("Enter the number of elements (N): "))

# Call the recursive function to calculate sum
result = sum_of_numbers_recursive(n)

# Output the result
print(f"The sum of the {n} numbers is: {result}")