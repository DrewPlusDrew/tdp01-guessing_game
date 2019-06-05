import random

#define constants
RANGE_BOTTOM = 1
RANGE_TOP = 10

#define functions
##define start_game(), the function that starts the game and carries out the gameplay itself
def start_game(high_score):
    print('''
    Welcome to the Number Guessing Game!
    ------------------------------------
    Try to guess the magic number.
    ''')
    answer = random.randrange(RANGE_BOTTOM, RANGE_TOP + 1)
    #print("The answer is", answer)  #for testing purposes
    num_attempts = 1
    while True:
        try:
            guess = int(input("Pick a number between {} and {}: ".format(RANGE_BOTTOM, RANGE_TOP)))
        except ValueError:
            print("Whoops, only numbers are accepted. Please enter a number.")
        else:
            if guess > RANGE_TOP:
                print("That guess is above the valid range, please try again.")
            elif guess < RANGE_BOTTOM:
                print("That guess is below the valid range, please try again.")
            elif guess > answer:
                print("The magic number is lower")
                num_attempts += 1
            elif answer > guess:
                print("The magic number is higher")
                num_attempts += 1
            else:
                print("That's correct! It took you {} attempt(s).".format(num_attempts))
                #if new high score, then tell user, give option to exit or play again
                if num_attempts < high_score:
                    high_score = num_attempts
                    print("WOW! THAT'S A NEW HIGH SCORE! The high score is now {}.  ".format(high_score))
                    ask_play_again(high_score)
                    break
                #if not new high score, just print current high score, give option to exit or play again
                elif num_attempts >= high_score:
                    print("The current high score is {}.".format(high_score))
                    ask_play_again(high_score)
                    break

##define ask_play_again(), a function that starts the game over if user says 'y' and ends it and prints high score if user says 'n'
def ask_play_again(high_score):
    play_again = input("Do you want to play again? y/n  ")
    if play_again[0].lower() == "y":
         start_game(high_score)
    else:
        print("Okay, that's the end of the game, bye.")
        print("The final high score for this round was {}.".format(high_score))


#start the game
if __name__ == '__main__':
    start_game(1000)
