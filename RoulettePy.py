import random

# Functions for managing red and black numbers
def reds():
    return [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

def blacks():
    return [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

# Function to simulate the game of roulette
def roulette():
    while True:  # Loop to allow replaying the game
        # Prompting the user to choose their bet
        choice = input("Choose what to bet on ( \n red/black \n even/odd \n 3) low/high \n 4) numbers: \n")
        # Asking the user to enter the amount they want to bet
        amount = float(input("Enter the amount in euros to bet: "))
        # Generating a random number between 0 and 36 (inclusive)
        number = random.randint(0, 36)
        # Checking if the bet is a win based on the chosen option
        win = (
            (choice == "red" and number in reds())    # Red numbers
            or (choice == "black" and number in blacks())   # Black numbers
            or (choice == "even" and number % 2 == 0)   # Even numbers
            or (choice == "odd" and number % 2 == 1)    # Odd numbers
            or (choice == "low" and 1 <= number <= 18)  # Numbers 1 to 18
            or (choice == "high" and 19 <= number <= 36)    # Numbers 19 to 36
            or (choice == str(number))     # Specific number chosen
        )
        # Handling the outcome of the bet
        if win:
            if number == 0:
                print(f"The 0 came out, the bank wins. You lost {amount}€")
            else:
                # Calculating the total win amount
                multiplier = 2 if choice in ("red", "black", "even", "odd", "low", "high") else 36
                total_win = amount * multiplier
                print(f"You win! The drawn number is {number}. You earned {total_win}€")
        else:
            if number == 0:
                print(f"The 0 came out, the bank wins.")
            else:
                print(f"You lost! The drawn number is {number}.")

        # Asking the user if they want to replay
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != "yes":
            break  # Exiting the loop if the user does not want to replay

# Calling the roulette function to start the game
roulette()
