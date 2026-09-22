num=int(input("Enter the number:"))
rev=0
n=num

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num//=10
if n==rev:
    print("Palindrome")
else:
    print("Not a palindrome")