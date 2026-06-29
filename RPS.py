import random

print("====================================")
print("     ROCK PAPER SCISSORS GAME")
print("====================================")

computer_score = 0
user_score = 0

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        user = "Rock"
    elif choice == "2":
        user = "Paper"
    elif choice == "3":
        user = "Scissors"
    else:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYour Choice     :", user)
    print("Computer Choice :", computer)

    if user == computer:
        print("Result : It's a Tie!")

    elif user == "Rock" and computer == "Scissors":
        print("Result : You Win!")
        user_score += 1

    elif user == "Paper" and computer == "Rock":
        print("Result : You Win!")
        user_score += 1

    elif user == "Scissors" and computer == "Paper":
        print("Result : You Win!")
        user_score += 1

    else:
        print("Result : Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        break

print("\n====================================")
print("            FINAL SCORE")
print("====================================")
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("\nOverall Winner : You")
elif computer_score > user_score:
    print("\nOverall Winner : Computer")
else:
    print("\nThe match ended in a Tie.")

print("\nThank you for playing!")