import autopy as ap
import screen_pixel
import time
import Quartz.CoreGraphics as CG

left_pos = False
right_pos = False


def right_btn():
    ap.key.tap(long(ap.key.K_RIGHT))
    time.sleep(.061)


def left_btn():
    ap.key.tap(long(ap.key.K_LEFT))
    time.sleep(.061)


def check_right_tree():
    sp = screen_pixel.ScreenPixel()
    region = CG.CGRectMake(1035, 290, 40, 40)
    sp.capture(region=region)
    # print sp.pixel(10, 20)
    # print sp.pixel(20, 20)
    # print sp.pixel(30, 20)
    if sp.pixel(20, 10) != (212, 247, 254, 255):
        return True
    else:
        return False


def check_left_tree():
    sp = screen_pixel.ScreenPixel()
    region = CG.CGRectMake(870, 290, 40, 40)
    sp.capture(region=region)
    # print sp.pixel(10, 20)
    # print sp.pixel(20, 20)
    # print sp.pixel(30, 20)
    if sp.pixel(20, 20) != (212, 247, 254, 255):
        return True
    else:
        return False


#############################################################################

if __name__ == "__main__":
    left_pos = True
    right_pos = False
    while True:
        if left_pos:
            if check_left_tree():
                # print "left tree!!!"
                right_btn()
                left_pos = False
                right_pos = True
            else:
                left_btn()
                left_pos = True
                right_pos = False
        else:
            if check_right_tree():
                # print "right tree!!"
                left_btn()
                left_pos = True
                right_pos = False
            else:
                # print "right btn"
                right_btn()
                left_pos = False
                right_pos = True
