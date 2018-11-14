
import simplegui
import random
import math
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


count = 7
rang = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    global secret_number, rang, count
    count = int(math.ceil(math.log(rang, 2)))
    secret_number = random.randrange(0, rang)
    print "New game. Range is [0,"+str(rang)+")"
    print "Number of remaining guesses is", count
    print
    
    return secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    global rang, count
    count = 7
    rang = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global rang, count
    count = 10
    rang = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here 
    
    global count, rang
    if count < 1:
        print "Game Over :("
        print
        new_game()
    else:
        count -= 1
        n = int(guess)
        if n >= rang:
            print str(n) + " is out of the range! Try another one"
            print
            return
        print "Guess was ", n
        print "Number of remaining guesses is ", count
        if secret_number > n:
            print "Higher!"
        elif secret_number < n:
            print "Lower!"
        else:
            print "Correct! :)"
        print

    
def reset():
    new_game()
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
f.add_input("Enter a guess", input_guess, 200)
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_button("Reset", reset, 200)

f.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
