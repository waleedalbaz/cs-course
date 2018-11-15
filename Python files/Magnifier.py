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

# classes
class ImageInfo():
    """
    container for all image info needed
    """
    def __init__(self, center, size):
        self.center = [center[0], center[1]]
        self.size = [size[0], size[1]]

    def get_center(self):
        """
        return image center value
        """
        return self.center

    def get_size(self):
        """
        return image size value
        """
        return self.size

class Magnifier():
    """
    create a magnifier glass
    """
    def __init__(self, image, pos, size):
        self.image = image
        self.pos = pos
        self.size = size
        self.degree = 3.0
        self.center = [self.degree*self.pos[0], self.degree*self.pos[1]]

    def set_pos(self, pos):
        self.pos = pos

    def set_degree(self, degree):
        """
        change the degree of zoomming
        """
        self.degree = degree #TODO

    def get_position(self):
        """
        get the position
        """
        return self.pos

    def get_degree(self):
        """
        get the degree of zoomming
        """
        return self.degree

    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size

# objects
# image info
image_info = ImageInfo(CENT_IMG, [W_IMG, H_IMG])

# magnifier
Magnifier_glass = Magnifier(image, MAG_POS, MAG_SIZE)

# event handlers
def click(pos):
    # global MAG_POS
    # MAG_POS = list(pos)
    Magnifier_glass.set_pos(list(pos))

def draw(canvas):
#    canvas.draw_image(image,
                  #    [W_IMG//2, H_IMG//2], [W_IMG, H_IMG],
                 #     [CANV_SIZE[0]//2, CANV_SIZE[1]//2],CANV_SIZE)
    canvas.draw_image(image, image_info.get_center(), image_info.get_size(),
                        [CANV_SIZE[0]//2, CANV_SIZE[1]//2], CANV_SIZE)
    # draw mag
    map_center = Magnifier_glass.get_center()
    map_rectangle = Magnifier_glass.get_size()
    mag_center = Magnifier_glass.get_position()
    mag_rectangle = Magnifier_glass.get_size()
    print "map_center: "+str(map_center)
    print "map_rectangle: "+str(map_rectangle)
    print "mag_rectangle: "+str(mag_rectangle)
    canvas.draw_image(image, map_center, [map_rectangle, map_rectangle],
                      mag_center, [mag_rectangle, mag_rectangle])

# create frame and its handler rigsters
f = simplegui.create_frame("Magnifier", CANV_SIZE[0], CANV_SIZE[1])
f.set_draw_handler(draw)
f.set_mouseclick_handler(click)

# start frame
f.start()