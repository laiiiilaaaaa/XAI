secret_word = "Machine Learning"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word:
    if guess_count <= guess_limit:
        guess = input("Enter your guess: ")
        print("Wrong guess!")
        guess_count += 1
    else:
        out_of_guesses = True
        break
if not out_of_guesses:
    print("You've guessed the word! The secret word is: " + guess + ". You've guessed it after: " + str(guess_count))
else:
    print("You've runed out of guesses")