# I'll do some OOP modifications
import simplegui

# global veriables
image = simplegui.load_image('https://cyprussite.com/img/map06.jpg')
#image dims
W_IMG = 3029
print "W_IMG", W_IMG
H_IMG = 2163
print "H_IMG", H_IMG
MAG_SIZE = 120
CENT_IMG = [W_IMG//2, H_IMG//2]
print 'CENT_IMG',CENT_IMG

SCALE = 3.0
CANV_SIZE = [W_IMG // SCALE, H_IMG // SCALE]
print 'CANV_SIZE', CANV_SIZE
CENT_CANV = [CANV_SIZE[0]/2, CANV_SIZE[1]//2]
print 'CENT_CANV', CENT_CANV
MAG_POS = [CANV_SIZE[0]//2, CANV_SIZE[1]//2]
print 'MAG_POS', MAG_POS
print "W =", CANV_SIZE[0]
print "H =", CANV_SIZE[1]

# class
class Magnifier()
def __init__(self, image, size, center):
	self.image = image
	self.size = [size[0], size[1]]
	self.center = [center[0], center[1]]

def set_degree(self, degree):
	pass


# event handlers
def click(pos):
    global MAG_POS
    MAG_POS = list(pos)

def draw(canvas):
    canvas.draw_image(image,
                      [W_IMG//2, H_IMG//2], [W_IMG, H_IMG],
                      [CANV_SIZE[0]//2, CANV_SIZE[1]//2],CANV_SIZE)
    # draw mag
    map_center = [SCALE * MAG_POS[0], SCALE * MAG_POS[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = MAG_POS
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image,
                      map_center, map_rectangle,
                      mag_center, mag_rectangle)

# create frame and its handler rigsters
f = simplegui.create_frame("Magnifier", CANV_SIZE[0], CANV_SIZE[1])
f.set_draw_handler(draw)
f.set_mouseclick_handler(click)

# start frame
f.start()