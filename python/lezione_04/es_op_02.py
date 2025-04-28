'''Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
import random

def guess_the_number():
    # Ask the user for the range of numbers and max attempts
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    max_attempts = int(input("Enter the maximum number of attempts: "))
    
    # Generate a random number within the specified range
    secret_number = random.randint(min_num, max_num)
    
    # Initialize the number of attempts taken
    attempts = 0
    
    print(f"\nI have generated a number between {min_num} and {max_num}. You have {max_attempts} attempts to guess it.")
    
    # Loop for user guesses
    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}: Guess the number: "))
        attempts += 1
        
        # Provide feedback based on the guess
        if guess < secret_number:
            print("Your guess is too low. Try again.")
        elif guess > secret_number:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
    else:
        print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

# Call the function to start the game
guess_the_number()



