# control the velocity of a ball using the arrow keys

import simplegui
import random


# Initialize globals
w = 600
h = 400
radius = 20

ball_pos = [w / 2, h / 2]
v = [0, 0]

color_arr = ["Red", "White", "Green", "Yellow", "Blue", "Gray"]
color = "White"

acc = 2
# define event handlers
def draw(canvas):
    global color
    # collide and reflect off
    if ball_pos[1] >= h - radius: # down
        v[1] = -v[1]
        color = random.choice(color_arr)
    elif ball_pos[0] <= radius:   # left
        v[0] = -v[0]
        color = random.choice(color_arr)
    elif ball_pos[0] >= w - radius: # right
        v[0] = -v[0]
        color = random.choice(color_arr)
    elif ball_pos[1] <= radius:  # up
        v[1] = -v[1]
        color = random.choice(color_arr)
    
    # Update ball position
    ball_pos[0] += v[0]
    ball_pos[1] += v[1]

    # Draw ball
    canvas.draw_circle(ball_pos, radius, 2, color, color)

def keydown(key):
    if key==simplegui.KEY_MAP["left"]:
        v[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        v[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        v[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        v[1] -= acc
        
    print ball_pos
    
def keyup(key):
    if key==simplegui.KEY_MAP["left"]:
        v[0] -= -acc
    elif key==simplegui.KEY_MAP["right"]:
        v[0] += -acc
    elif key==simplegui.KEY_MAP["down"]:
        v[1] += -acc
    elif key==simplegui.KEY_MAP["up"]:
        v[1] -= -acc
        
    print ball_pos


# create frame 
frame = simplegui.create_frame("Velocity ball control", w, h)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
