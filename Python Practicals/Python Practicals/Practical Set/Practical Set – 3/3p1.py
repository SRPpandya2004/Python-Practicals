# 1 WAP to find sum of first N numbers

num=int(input("Enter the num:"))
print(num)

def sum(n):
    
    return n*(n+1)/2
    #return n*(n+1)//2


print("The sum of ",num," is = ",sum(num) )


#____________________________USing Recursion_______________________________




def sum_num(n1):
    if n1==0:
        return 0
    else:
        return n1 +sum_num(n1-1)

print(f"The sum of new {num} is = {sum_num(num)} ")