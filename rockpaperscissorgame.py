import random

# CREATED 12.21.19
hands = ["rock", "paper", "scissors"]
choices = 0
player_points = 0
computer_points = 0
rounds = 5
# goes up to five rounds for player
while rounds > 0:
    computer_choice = random.choice(hands)
    player_choice = input("Please choose rock, paper, or scissors").lower().strip()
    if player_choice == computer_choice:  # computer and player choice are same
        print("Try again, you guys got the same thing!\n")
    elif player_choice == "rock":  # player chooses rock.
        if computer_choice == "scissors":
            player_points += 1
            print(player_choice, "beats: ", computer_choice, ". You won this round.\n")
            rounds -= 1
        else:  # computer chose paper
            computer_points += 1
            print("Computer chose: ", computer_choice, "Better luck next time.\n")
            rounds -= 1
    elif player_choice == "paper":  # player chooses paper
        if computer_choice == "rock":
            computer_points += 1
            print("Computer chose: ", computer_choice, "Better luck next time!\n")
            rounds -= 1
        else:  # computer chose scissors
            player_points += 1
            print(player_choice, "beats: ", computer_choice, "You won this round.\n")
            rounds -= 1
    elif player_choice == "scissors":  # player chooses scissors
        if computer_choice == "rock":
            print("Computer chose:", computer_choice, ". Better luck next time!\n")
            rounds -= 1
        else:  # computer chose paper, you chose scissors:
            player_points += 1
            print(player_choice, "beats", computer_choice, "You won this round.\n")
            rounds -= 1
    else:  # player chooses something that is not paper, scissors, or rock
        print("Please choose rock, paper, scissors.\n")

if player_points > computer_points:
    print(f'Congratulations, You won the game.\nYou got {player_points} points.\nComputer got {computer_points} points.')
elif computer_points > player_points:
    print(f'Better luck next time, You lose the game.\nYou got {player_points} points.\nComputer got {computer_points} points.')
