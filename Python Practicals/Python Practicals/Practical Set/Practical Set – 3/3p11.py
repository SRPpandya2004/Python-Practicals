"""# 11 WAP to print the following:
    1)  1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5     """

# num = int(input("Enter Number = "))

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print(" ")


"""2)   * * * * *
        * * * * 
        * * *
        * *
        *     """

for row in range(1,6):
    for col in range(row-1,5):
        print("*",end=" ")
    print(" ")