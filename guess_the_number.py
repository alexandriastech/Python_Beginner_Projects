import random


golden_number = random.randint(0, 20)
count = 0
guess = 3

while count != guess:
    choice = int(input("Input a random number from 1 to 20: "))
    if choice == golden_number:
        print("Congratulations, you've found the golden number!")
        break
    elif choice < golden_number:
        count += 1
        print(f"Your number is too low! You have {guess-count} left!")
    elif choice > golden_number:
        count += 1
        print(f"Your number is too large! You have {guess-count} left")
    elif choice > 20 or choice < 1:
        print("Invalid input")

        
