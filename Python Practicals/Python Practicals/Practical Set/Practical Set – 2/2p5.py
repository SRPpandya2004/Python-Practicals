# 5 WAP to find maximum of three numbers (nested if-else).

print("FInd the MAximum of Three num")

n1=int(input("Enter First number = "))
n2=int(input("Enter Second number = "))
n3=int(input("Enter Third number = "))

# if n1>n2 and n1>n3:
#     print(n1," First is Maximum")
# elif n2>n1 and n2>n3:
#     print(n2,"Second is Maximum")
# else:
#     print(n3,"Third is Maximum")


if n1>n2:

    if n1>n3:
        print(n1," First is Maximum")
    else:
        print(n3,"Third is Maximum")

elif n2>n1:
    
    if n2>n3:
        print(n2,"Second is Maximum")
    else:
        print(n3,"Third is Maximum")

else:
    print("Two or more num are same value")