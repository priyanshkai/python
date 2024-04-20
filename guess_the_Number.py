import random

# Set game parameters
secret_number = random.randint(1, 100)
guesses_allowed = 5

# Welcome message
print("Welcome to the Guessing Game!")

# Game loop
while guesses_allowed > 0:
  # Get player guess
  guess = int(input("Guess a number between 1 and 100: "))
  guesses_allowed -= 1

  # Check guess
  if guess == secret_number:
    print("Congratulations! You guessed the number!")
    break  # Exit the loop on correct guess
  elif guess < secret_number:
    print("Your guess is too low. Try again!")
  else:
    print("Your guess is too high. Try again!")

# Game over message
if guesses_allowed == 0:
  print("You ran out of guesses. The secret number was", secret_number)

print("Thanks for playing!")
