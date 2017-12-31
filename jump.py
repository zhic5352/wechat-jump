# -*- coding: utf-8 -*-

import cv2
import adbCmd
import math

# flag draw line
doAction = False
# mouse end point
xEnd, yEnd = 0, 0
# mouse start point
xStart, yStart = 0, 0
# press factor, using for calculator a duration to press
factor = 1.32
# image show title
IMG_TITLE = "imgTile"
# path on android device
REMOTE_PATH = "/sdcard/aJump.jpg"
# path on local pc
LOCAL_PATH = "d:/tmp/python/picTest.jpg"


def draw_line(event,x,y,flags,param):
    global xStart,yStart,xEnd,yEnd,factor
    if event == cv2.EVENT_LBUTTONDOWN:
        doAction = False
        xStart, yStart = x, y
        print xStart, yStart
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        pass
    elif event == cv2.EVENT_LBUTTONUP:
        doAction = True
        xEnd, yEnd = x, y
        print "xStart:%s,yStart:%s  xEnd:%s,yEnd:%s"%(xStart, yStart, xEnd, yEnd)
        do_press(get_weight(xStart, yStart, xEnd, yEnd, factor))
    else:
        pass

def get_picture(remote_path, local_path):
    adbCmd.screencap(remote_path, local_path)
    
def do_press(weight):
    adbCmd.action_press(weight)

def resize_img(img):
    # here is a 1080x1920 device
    # when the ROI is (x[0,1080],y[500,1200])(start from top-left)
    return img[500:1200, 0:1080]

def get_weight(x1,y1,x2,y2,factor):
    return int(factor*math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2))

if __name__ == '__main__':
    while(1):
        #get picture from android device
        get_picture(REMOTE_PATH, LOCAL_PATH)
        #load image
        image = resize_img(cv2.imread(LOCAL_PATH))
        cv2.imshow(IMG_TITLE, image)
        cv2.setMouseCallback(IMG_TITLE, draw_line)

        while(1):
            cv2.imshow(IMG_TITLE, image)
            #press SPACE get the next picture
            if cv2.waitKey(20)&0xFF==32:
                break
            #press ESC exit the loop
            if cv2.waitKey(20)&0xFF==27:
                cv2.destroyAllWindows()
                print 'Good game!'
                exit(0)