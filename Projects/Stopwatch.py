import simplegui
# template for "Stopwatch: The Game"

# define global variables
w = 200 # width
h = 200 # height
total = 0 # estimated time
s_stops = 0 # successful stops
total_stops = 0 # stopped times
is_stopped = False # is Stopwatch stopped or running?


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    leading = ":0"
    min = t // 600
    sec = (t // 10) % 60
    tes = t % 10
    if sec >= 10:
        leading = ":"
    result = "0" + str(min) + leading + str(sec) + "." + str(tes)
    
    return result  

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_stopped
    t.start()
    is_stopped = False
    

def stop():
    global s_stops, total_stops, is_stopped
    if not is_stopped:
        total_stops += 1
        if total % 10 == 0:
            s_stops += 1
    t.stop()
    is_stopped = True

def reset():
    global total, is_stopped, total_stops, s_stops
    is_stopped = True
    t.stop()
    total = 0
    s_stops = 0
    total_stops = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global total
    total += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(format(total), [w/3, h/2], 24, "White")
    canvas.draw_text(str(s_stops) + "/" + str(total_stops), [w * 0.8, h * 0.1], 18, "yellow")

    
# create frame
f = simplegui.create_frame("Stopwatch", w, h)
t = simplegui.create_timer(100, tick)

# register event handlers
f.set_draw_handler(draw)
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)

# start frame
f.start()


# Please remember to review the grading rubric
