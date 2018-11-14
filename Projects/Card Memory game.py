# implementation of card game - Memory

import simplegui
import random

list1 = [0, 1, 2, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 6, 7]
co_list = list1 + list2
print co_list
random.shuffle(co_list)
print co_list
w_card = 50
h_card = 100
# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global co_list
    count = 0
    for n in co_list:
        count += 1
        canvas.draw_text(str(n), [50 * count, 70], 60, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric