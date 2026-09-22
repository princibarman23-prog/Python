n=int(input("Enter a number:"))

prime = True
if n<= 1:
    prime = False
else:
    for i in range(2,n):
        if n%i == 0:
            prime = False
            break
if prime:
    print("Prime Numbers")
else:
     print("Not a prime number")