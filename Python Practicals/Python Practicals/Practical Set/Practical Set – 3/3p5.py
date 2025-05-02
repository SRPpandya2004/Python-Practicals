# 5 WAP to find the reverse of given numbers (Example 2564-4652).


num =int(input("Enter Num = "))

def rev(num):

    rev=0
    while num>0:
                
        rem=num%10
        rev= rev*10 + rem 
        num=num//10
    return rev
    
print(f"The reverse num of {num} = {rev(num)}")

#_______________________________Method 2____________________________________________

reverse = int(str(num)[::-1])

print(f"The reverse num of {num} = {reverse}")