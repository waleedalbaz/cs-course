# I'll do some OOP modifications
import simplegui

# global veriables
image = simplegui.load_image('https://cyprussite.com/img/map06.jpg')
#image dims
W_IMG = 3029
H_IMG = 2163

MAG_SIZE = 120
CENT_IMG = [W_IMG//2, H_IMG//2]
SCALE = 3.0
CANV_SIZE = [W_IMG // SCALE, H_IMG // SCALE]
CENT_CANV = [CANV_SIZE[0]/2, CANV_SIZE[1]//2]
MAG_POS = [CANV_SIZE[0]//2, CANV_SIZE[1]//2]

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

    def draw_org_image(self, canvas):
        img_center = self.get_center()
        img_size = self.get_size()
        canv_center = [CANV_SIZE[0]//2, CANV_SIZE[1]//2]
        canvas.draw_image(image, img_center, img_size,
                          canv_center, CANV_SIZE)


class Magnifier():
    """
    create a magnifier glass
    """
    def __init__(self, image, pos, size):
        self.image = image
        self.pos = [pos[0], pos[1]]
        self.size = size
        self.degree = 3.0
        #self.center = [self.pos[0]*self.degree, self.pos[1]*self.degree]

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

    def draw_magnifier(self, canvas):
        center1 = [self.get_position()[0]*self.degree,
                    self.get_position()[1]*self.degree]
        center2 = self.get_position()
        size = self.get_size()
        canvas.draw_image(image, center1, size, center2, size)

# objects
# image info
image_info = ImageInfo(CENT_IMG, [W_IMG, H_IMG])

# magnifier
Magnifier_glass = Magnifier(image, MAG_POS, [MAG_SIZE, MAG_SIZE])

# event handlers
def click(pos):
    Magnifier_glass.set_pos(list(pos))

def draw(canvas):
    # draw orignal image
    image_info.draw_org_image(canvas)

    # draw mag
    Magnifier_glass.draw_magnifier(canvas)

# create frame and its handler rigsters
f = simplegui.create_frame("Magnifier", CANV_SIZE[0], CANV_SIZE[1])
f.set_draw_handler(draw)
f.set_mouseclick_handler(click)

# start frame
f.start()

