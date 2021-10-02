# random number guess game
import random
def main():
    guess_num = random.randint(0, 10)
    guess = ""
    guess_limit = 3
    guess_count = 0
    out_of_guesses = False
    while guess != guess_num and not out_of_guesses:
        if guess_count < guess_limit:
            # Handle any error in case the user enters a value that is neither a number nor an integer number.
            try:
                guess = int(input("Guess a number between 0-10: "))
                # Help give the gamer the hint about the the guess number.
                if guess > guess_num:
                    print("Try lower")
                elif guess < guess_num:
                    print("Try higher")
            except:
                print("The value entered is not an integer!")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        # This means that the user has not gotten the right answer and is out of guesses.
        print("Out of guesses, YOU LOSE!\n")
        # Prompt the user in case they want to play again after loosing.
        print("Would you like to try again?")
        answer = input("Enter a y/n: ").lower()
        if answer == "y":
            # If a yes answer is chosen, the program loops an starts again
            main()
        elif answer == "n":
            # Display text in case the gamer chooses 'no' for an answer.
            print("Thank you for playing, GOODBYE!")
        else:
            # Handle any error in case the user inputs an answer that is neither a 'yes' or 'no'.
            print("Invalid input!!\n")
    else:
        # Display text when the gamer guesses the right number.
        print("YOU WIN!")
        print("Would you like to play again?")
        answer = input("Enter a y/n: ").lower()
        if answer == "y":
            main()
        elif answer == "n":
            print("Thank you for playing, GOODBYE!")
        else:
            print("Invalid input!!")
main()


