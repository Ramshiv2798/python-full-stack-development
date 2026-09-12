# task 1

import random
def play_rps():
    """Rock, Paper, Scissors game / returns 0 = tie, 1 = you won, 2 = computer won"""
    user1_score, user2_score = 0, 0
    user1_choice = input("Enter one of these --> rock, paper, scissors: ").lower().strip()
    user2_choice = random.choice(["rock", "paper", "scissors"]).lower()

    if user1_choice not in ["rock", "paper", "scissors"]:
        print("Enter a valid choice: rock/paper/scissors")
        return play_rps()

    print("user1:", user1_choice, "| user2:", user2_choice)

    if (user1_choice == 'rock' and user2_choice == "paper") or \
       (user1_choice == "paper" and user2_choice == "scissors") or \
       (user1_choice == "scissors" and user2_choice == "rock"):
        return 2
    elif user1_choice == user2_choice:
        return 0
    else:
        return 1

user1_points, user2_points = 0, 0
for _ in range(10):
    result = play_rps()
    if result == 1:
        print("user1 is won")
        user1_points += 1
    elif result == 0:
        print("Tie")
    else:
        print("user2 won this round")
        user2_points += 1

print("-----------------------")
print(f"Final Score: You = {user1_points}, user2 = {user2_points}")
if user1_points > user2_points:
    print(" user1 is won")
elif user2_points > user1_points:
    print(" user2 wins a point")
else:
    print(" Both are equal — Tie")

# task 2
def play_number_guess():
    
    won = False
    max_range = 20
    for attempt in range(3):
        guess = int(input(f"Guess the number between 1 and {max_range}: "))
        target = random.randint(1, max_range)

        if guess < 1 or guess > max_range:
            print("Invalid input! Enter within the range. Restarting...")
            return play_number_guess()

        print("You guessed:", guess, "| Actual:", target)

        if guess == target:
            print(" You won the game!")
            won = True
            break
        else:
            print("Try again...")
            max_range = max_range - max_range // 2

    if not won:
        print(" You lost all chances. Go and study!")

choice = ""
while choice != '3':
    choice = input("""Choose your game:
    1. Rock, Paper, Scissors
    2. Number Guessing
    3. Exit to Study
    Enter 1/2/3: """)

    if choice == '1':
        result = play_rps()
        if result == 1:
            print("You are the winner")
        elif result == 0:
            print("Tie")
        else:
            print("Computer is the winner")
    elif choice == '2':
        play_number_guess()
    elif choice == '3':
        print(" Time to study, focus well!")
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
