# 7 WAP to check whether entered input is character, digit or special symbol using ladder if-else

key = input("Enter key : ")


if len(key)==1 and key.isalpha():
    print(key,"is charecter")

elif key.isalpha():
    print(key,"is String")
    
elif key.isdigit():  #additional part to find string
    print(key," is Digit")

else:
    print(key,"is Special Symbol")

