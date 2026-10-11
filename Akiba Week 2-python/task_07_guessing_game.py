
secret_number = 7
attempts = 5
attempts_number = 0

while attempts > 0:
    print("Attempts remaining:", attempts)
    guess = int(input("Guess the Number: "))

    attempts -= 1
    attempts_number += 1

    if guess == secret_number:
        print("Congratulations!")
        print(f"You guessed the number in {attempts_number} attempts.")
        break
    else:
        print("Wrong guess! Try again.")

if attempts == 0 and guess != secret_number:
    print("Game Over! The secret number was", secret_number)

print("Total guesses:", attempts_number)
