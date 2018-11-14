# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random


# initialize global variables
num_range = 100


# helper function to start and restart the game
def new_game():
    global secret_number, count
    secret_number = random.randrange(0, num_range)
    print "New game. Range is from 0 to", num_range
    count = int(math.ceil(math.log(num_range, 2)))
    print "Number of remaining guesses is", count
    print # new line


# define event handlers for control panel
def restart():
    """button that resets the game"""
    
    new_game()

def range100():
    """button that changes the range to [0,100) and starts a new game"""
    
    global num_range
    num_range = 100
    new_game()

def range1000():
    """button that changes the range to [0,1000) and starts a new game"""
    
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    """main game logic goes here"""
    
    global count
    num = int(guess)
    print "Guess was " + str(num)
    count -= 1
    print "Number of remaining guesses is", count
    if (secret_number > num) and (count > 0):
        print "higher!"
        print # new line
    elif (secret_number < num) and (count > 0):
        print "Lower!"
        print # new line
    elif secret_number == num:
        print "Correct!"
        print # new line
        new_game()
    else:
        print "You ran out of Guesses. The number was", secret_number
        print # new line
        new_game()
    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
f.add_input("Enter a guess", input_guess, 200)
f.add_button("Restart", restart, 200)
f.add_button("Range is [0,100]", range100, 200)
f.add_button("Range is [0,1000]", range1000, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
