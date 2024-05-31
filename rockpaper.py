import random

def print_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

def main():
    print("\n===== Rock, Paper, Scissors =====")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice: ")

    while choice == '1':
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        print_result(user_choice, computer_choice)

        print("\n1. Play Again")
        print("2. Exit")
        choice = input("Enter your choice: ")

    if choice == '2':
        print("Exiting the Rock, Paper, Scissors game.")

if __name__ == "__main__":
    main()