import random

# CREATED 12.21.19
hands = ["rock", "paper", "scissors"]
choices = 0
tries = 3
player_points = 0
computer_points = 0
# goes up to five rounds for player
while player_points != 5:
    computer_choice = random.choice(hands)
    player_choice = input("Please choose rock, paper, or scissors: ").lower().strip()
    if player_choice == computer_choice:  # computer and player choice are same
        print(computer_choice)
        print("Try again, you guys got the same thing!\n")
    elif player_choice == "rock":  #-----------------------------player choice: rock
        if computer_choice == "scissors": #computer choice scissors
            player_points += 1
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. You won this round.")
        else:  # computer chose paper
            computer_points += 1
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. Better luck next time.")
    elif player_choice == "paper":  #-----------------------------player choice: paper
        if computer_choice == "rock": #computer choice: rock
            computer_points += 1
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. Better luck next time!")
        else:  # computer chose scissors
            player_points += 1
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. You won this round.")
    elif player_choice == "scissors":  # -------------------------player chooses scissors
        if computer_choice == "rock":
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. Better luck next time!")
        else:  # computer chose paper, you chose scissors:
            player_points += 1
            print(f"Player choice: {player_choice}. Computer choice: {computer_choice}. You won this round.")
    else:  # player chooses something that is not paper, scissors, or rock
        print("Please choose rock, paper, scissors.\n")

print("Congratulations, you've won a total of: ", player_points, "rounds")
print("The computer has won: ", computer_points, "rounds")
