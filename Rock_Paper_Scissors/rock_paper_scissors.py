import random

print("===== Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
    else:
        print("😔 Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break