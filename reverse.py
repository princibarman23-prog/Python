num=int(input("enter the number to be reversed:"));
rev=0;
while num>0:
    rem = num%10;
    rev=(rev*10)+rem;
    num//=10;
print("Reverse number is:",rev);