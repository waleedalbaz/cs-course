import simplegui


# Global variables
value = "Waleed"
# Helper function
def pig_latin(word):
    first_word = word[0]
    raiming_word = word[1:]
    
    # the game logic aeiou
    if first_word in "aeiou":
        return first_word + raiming_word + "way"
    else:
        first_word = ""
        return raiming_word + word[0] + "ay"
        

# Handlers functions
def draw(canvas):
    canvas.draw_text(value, [80, 100], 21, "Red")
    #canvas.draw_line([105, 105], [160, 105], 3, "Yellow")

def input_field(t):
    global value
    value = pig_latin(t)

    
# create frame & its handlers
f = simplegui.create_frame("Test Canvas", 200, 200)
f.set_draw_handler(draw)
f.add_input("Enter a name", input_field, 200)

# start the frame
f.start()
