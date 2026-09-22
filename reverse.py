num=int(input("Enter the numbert to be reversed:"))
rev=0
while num > 0:
    rem=num%10
    rev=(rev*10)+rem
    num//=10
print("Reversed number is:",rev)
