import random
n=int(input("Enter the range:"))
sec_num= random.randint(1,n)
attempts=0
max_att=5

print("===============================================")
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between the given range.")
print(f"You have{max_att} chances to guess it.")
print("===============================================")

while attempts < max_att:
    attempts = attempts + 1
    remaining = max_att - attempts

    guess=input(f"\n[Attempt {attempts}] Enter your guess:")
    guess=int(guess)

    if guess == sec_num:
        print(f"Correct! You guessed the number in {attempts} attempts!")
        break
    elif guess < sec_num:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print(f"Chances left:{remaining}")

if guess != sec_num:
    print("\n Game Over!")
    print(f"The correct answer was {sec_num}.\n Better Luck Next Time.")