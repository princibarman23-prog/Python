a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))

if(a>=b and a>=c):
    print("Largest number is:",a)
elif(b>=a and b>=c):
    print("Largest number is:",b)
else:
    print("Largest number is:",c)