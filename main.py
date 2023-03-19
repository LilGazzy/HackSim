import random

def generate_code():
    """Generate a random 4-digit code."""
    code = ""
    for i in range(4):
        code += str(random.randint(0, 9))
    return code

def play_game():
    """Play the game."""
    print("Welcome to Terminal Hacker Simulator!")
    print("You have to guess a 4-digit code.")
    print("Enter 'q' to quit.")
    code = generate_code()
    while True:
        guess = input("Enter your guess: ")
        if guess == "q":
            print("Quitting the game...")
            break
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        if guess == code:
            print("Congratulations! You have hacked the system!")
            break
        else:
            num_correct = 0
            for i in range(4):
                if guess[i] == code[i]:
                    num_correct += 1
            print(f"Sorry, that is not the correct code. {num_correct} digits are correct.")

play_game()
