# 6 WAP to check whether entered number is prime or not.

# def prime(n):
#     if n<=0:
#         return False
#     for i in range(2,int (n**0.5) +1 ):
#             if n % i == 0:
#                 return False
#     return True

# num=int(input("Enter NUmber = "))

# if prime(num)==True:
#      print("Num is Prime")
# else:
#      print("Num is Not Prime")
# Function to calculate salary based on degree and experience
def calculate_salary(degree, experience):
    if degree == "B.E.":
        if experience < 5:
            salary = 30000
        else:
            salary = 40000
    elif degree == "M.E.":
        if experience < 5:
            salary = 50000
        else:
            salary = 60000
    else:
        salary = "Invalid degree"

    return salary

# Input from user
degree = input("Enter your degree (B.E. or M.E.): ")
experience = int(input("Enter your years of experience: "))

# Calculate and print the salary
salary = calculate_salary(degree, experience)
print(f"The salary is: {salary}")
