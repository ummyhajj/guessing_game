# This is a boilerplate source code to get you up to speed quickly
# with the game. Key functions are defined for you so your duty is
# just to fill them with the code neccessary. Feel free to rename
# the functions if you're not happy with the names. You can also add
# as many functions as you need. Finally, you might want to delete
# this comment block before submitting your work. Happy coding!
import sys
import random
def get_user_input(prompt: str) -> str:
    sys.stdin.read()
    random.radiant(1 , 5)
    min_guess = 1
    max_guess = 5
    user_input = int(input("Please predict a number"))

    
    """
        Reads user input from the standard input.

        Parameters
        ----------
        prompt
            the prompt message
        Returns
        -------
        str 
           the user input
    """
    # strip() removes any leading or trailing whitespace from the input
    return user_input.strip()


def generate_random_number(min: int = 0, max: int = 100) -> int:

        
    """
        Generates a random integer that is at least {min} and at most {max}

        Parameters
        ----------
        min
            The mininum number for the generated number, defaults to 0
        max
            The maximum number for the generated number, defaults to 100

        Return
        ------
        int
            The generated number. The number is such that: min<= number <=max.
    """

    # Implement get_random_number(min,max) 
    # make sure that the resulting random number is at least the min and
    # at most the max value. The random module in the standard library may be helpful
    random_number =  get_random_number(min,max)

    return random_number


#######s####### Don't modify anything in this block ######################################################

def print_welcome_message():
    welcome_message = " Welcome to GuessMe. GuessMe is a simple game that asks you to guess a secrete number,\n you're then told if you guessed right or wrong. To quit this game, type <CTR> + C"
    print(welcome_message)
    print("\n\n Version 1.0 \n\n")


def start_game():
    "Starting point of the game. It first prints a welcome message and enters into an infinite loop"

    min_guess = 1
    max_guess = 5
    print_welcome_message()

    # Begin Game

    while True:
        random_number = generate_random_number(1, 5)
        guessed_number = get_user_input(f"Please enter a number between {min_guess} - {max_guess} and press enter > ")
    333333333    if int(guessed_number) == random_number:
            print("Congrats! you guessed right :-)")
        else:
            print(
                f"Oh snap! you missed that, correct number was {random_number} :-(")

    # End Game

    print("Exiting game, sad to see you go :-(")
#End start_game


if __name__ == "__main__":
    start_game()

############### End block ################################################
