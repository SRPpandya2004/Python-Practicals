# 6
"""WAP to calculate the salary of an employee based on following conditions
    (nested if-else):
    1. if degree = B.E. and experience < 5 years, salary=30000
    2. if degree = B.E. and experience >= 5 years, salary=40000
    3. if degree = M.E. and experience < 5 years, salary=50000
    4. if degree = M.E. and experience >= 5 years, salary= 60000"""

print("Select degree : \n 1 = B.E \n 2 = M.E")

degree = int(input("Enter Chice = "))

if degree==1:
    print("Choosen degree = B.E")
elif degree==2:
    print("Choosen degree = M.E")
else:
    print("Enter Valid Choice")
    

experience = int(input("Enter Experience = "))

if degree==1:
    if experience < 5 :
        print("The Salary = 30000")
    else:
        print("The Salary = 40000")

if degree==2:
    if experience < 5 :
        print("The Salary = 50000")
    else:
        print("The Salary = 60000")