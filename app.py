import autopy as ap
import screen_pixel
import time
import Quartz.CoreGraphics as CG
from autopy.mouse import LEFT_BUTTON
from pngcanvas import PNGCanvas
from PIL import Image
from pytesseract import *

black = (0, 0, 0, 255)


def left_click():
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.5)


def move_xy(x, y):
    ap.mouse.move(x, y)
    time.sleep(.2)


def get_diff():
    image_name = 'diff.png'
    get_rect(840, 250, 280, 80, image_name)
    return get_text_from_image(image_name)


def get_answer():
    image_name = 'answer.png'
    get_rect(840, 310, 280, 80, image_name)
    return get_text_from_image(image_name)


def get_text_from_image(image_name):
    im = Image.open(image_name)
    text = image_to_string(im)
    return text


def get_rect(x, y, width, height, image_name):
    region = CG.CGRectMake(x, y, width, height)
    sp = screen_pixel.ScreenPixel()
    sp.capture(region)
    save_image(sp, image_name)


def save_image(sp, image_name):
    c = PNGCanvas(sp.width, sp.height)
    for x in range(sp.width):
        for y in range(sp.height):
            c.point(x, y, color=sp.pixel(x, y))

    with open(image_name, "wb") as f:
        f.write(c.dump())


#############################################################################

if __name__ == "__main__":
    print get_diff()
    print get_answer()
    # image_file = 'test.png'
    # im = Image.open(image_file)
    # text = image_to_string(im)
    # print "=====output=======\n"
    # print text
