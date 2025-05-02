# 7 WAP to print all even numbers between 1 to n except the numbers divisible by 6.

num = int(input("Enter Rangr of Num: "))

def even6(num):
    for el in range(1,num):
        if el%2==0 and el%6!=0:
                print(el ,end=" ")
    
even6(num) 

print(f"are even numbers between 1 to {num} except the numbers divisible by 6")

        
