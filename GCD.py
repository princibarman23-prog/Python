a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
while b!=0:
    a,b=b,a%b

print("Greatest number:",a)