
num= int(input("Enter the num = "))

def fact(n):

    if n==0 or n==1:
        return 1
    elif n<0:
        print("Factorial Does not Exis for negative num")
    else:
        return n*fact(n-1)
    

print("The factorial of ",num," is = ",fact(num) )




# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = 7

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))
