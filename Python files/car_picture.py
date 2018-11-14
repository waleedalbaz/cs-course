import simplegui
#def fet2cels(f):
#    return (5/9.0) * (f - 32)
#
#def cels2feh(c):
#    return c/(5/9.0) + 32
#
#print fet2cels(116.6)
#print cels2feh(47)
#print 5/9.0
##c = (5/9.0) * (f - 32)
##c/(5/9.0) = (f - 32)
##f = c/(5/9.0) + 32


def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    canvas.draw_line([50, 180], [250, 180], 40, "Red")
    canvas.draw_line([55, 170], [90, 120], 5, "Red")
    canvas.draw_line([90, 120], [130, 120], 5, "Red")
    canvas.draw_line([180, 108], [180, 160], 140, "Red")
    

f = simplegui.create_frame("The answer", 300, 300)
f.set_draw_handler(draw)
f.start()