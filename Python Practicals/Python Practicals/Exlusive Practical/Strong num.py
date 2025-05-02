#Check the number is Strong num or not


num =int(input("Enter Num ="))

print("Your enterd num = ",num)

def strongnum(num):

    if num==digit(num):
        print("The Num is Strong num")
    
    else:
        print("The Num is____ Not ____Strong num")
     
    
def digit(num):
    sum=0
    y=str(num)

    for el in y:
        z=int(el)
        sum+=fact(z)
        # print(fact(z))
    
    return sum


def fact(x):
    val = 1
    
   
    if x==1 or x==0:
        return 1
    
    else:
        while x>=1 :
            val *= x
            x-=1
        return val

strongnum(num)

# print(digit(40585))

# x=152

# xn=str(x)

# print(xn[1])

