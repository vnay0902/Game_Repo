import random

# Function to determine the winner
def winner(user, computer):
    if user == computer:
        return "tie"
    elif user == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "user"
    elif user == "paper":
        if computer == "scissors":
            return "computer"
        else:
            return "user"
    elif user == "scissors":
        if computer == "rock":
            return "computer"
        else:
            return "user"
    else:
        return "invalid input"

# Function to determine the computer's choice
def computer_choice():
    computer = random.choice(["rock", "paper", "scissors"])
    return computer

# Function to determine the user's choice
def user_choice():
    while True:
        user = input("Enter your choice (rock/paper/scissors): ").lower()
        if user in ["rock", "paper", "scissors"]:
            return user
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

# Function to play the game
def play_game():
    user = user_choice()
    computer = computer_choice()
    print("You chose", user)
    print("The computer chose", computer)
    print("The winner is", winner(user, computer))

# Function to play the game again
def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").lower()
        if answer == "yes":
            play_game()
        elif answer == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main function
def main():
    play_game()
    play_again()

main()
