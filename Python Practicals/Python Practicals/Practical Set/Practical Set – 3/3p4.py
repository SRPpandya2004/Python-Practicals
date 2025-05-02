# 4 Write a Python program to print Fibonacci series upto n terms

# Function to print Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    # Print the first two terms if n is greater than or equal to 1
    if n >= 1:
        print(a, end=" ")
    # Print the series up to n terms
    for _ in range(1, n):
        print(b, end=" ")
        a, b = b, a + b  # Update values of a and b for the next term

# Input: number of terms to print
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Call the function to print Fibonacci series
fibonacci(n)