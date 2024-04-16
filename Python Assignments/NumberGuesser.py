import random

def guess_number_game():
    low = 1
    high = 50
    correct_answer = random.randint(low, high)
    
    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between {low} and {high}. You have 5 chances to guess it.")
    
    for _ in range(5):
        guess = int(input("Enter your guess: "))
        
        if guess == correct_answer:
            print("Congratulations! You win!")
            return
        elif guess < correct_answer:
            print("The correct answer is greater.")
        else:
            print("The correct answer is smaller.")
    
    print(f"Sorry, you've run out of guesses. The correct answer was {correct_answer}. You lose.")

# Run the game
guess_number_game()
