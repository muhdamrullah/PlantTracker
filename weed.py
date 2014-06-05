'''
This is how to track a white ball example using SimpleCV

The parameters may need to be adjusted to match the RGB color
of your object.

The demo video can be found at:

'''
print __doc__

import SimpleCV

display = SimpleCV.Display() #create the display to show the image
cam = SimpleCV.Camera() # initalize the camera
normaldisplay = True # mode toggle for segment detection and display

while display.isNotDone(): # loop until we tell the program to stop

    if display.mouseRight: # if right mouse clicked, change mode
        normaldisplay = not(normaldisplay)
        print "Display Mode:", "Normal" if normaldisplay else "Segmented"

    img = cam.getImage().flipHorizontal() # grab image from camera
    weed = img.crop(320,240,50,50)
    green_weed = img.colorDistance(SimpleCV.Color.GREEN)
    on_weed = img - green_weed
    only_weed = on_weed * 10
    print only_weed.meanColor() 
    white = only_weed.binarize()
    black = white.invert()
    blobs = black.findBlobs()
    print blobs[-1].area()
#    R,G,B = only_weed.splitChannels(False)
#    if R < 1 and B < 1 and G > 5:
#        print only_weed.meanColor()
#    if weed:
#        img.drawMinRect(color=SimpleCV.Color.RED, width=-1,alpha=128)
#    R,G,B = img.splitChannels(False)
#    if R < 1 and B < 1 and G > 5 and green_blobs:
#       img.drawCircle((green_blobs[-1].x, green_blobs[-1].y), green_blobs[-1].radius(),SimpleCV.Color.BLUE,3)
#    print only_weed.meanColor()
#    green_stuff = img.colorDistance(SimpleCV.Color.GREEN).dilate(2)
#    green_stuff = green_plant.stretch(200,255)
#    green_blobs = green_stuff.findBlobs()
#    green_blobs[-1].draw(color=SimpleCV.Color.GREEN,width=-1,alpha=238)
#    if green_blobs:   
#           img.drawCircle((green_blobs[-1].x, green_blobs[-1].y), green_blobs[-1].radius(),SimpleCV.Color.GREEN,3)
#    print "largest green blob at " + str(green_blobs[-1].x) + ", " + str( green_blobs[-1].y)

#    dist = img.colorDistance(SimpleCV.Color.RED).dilate(2) # try to separate colors in image
#    segmented = dist.stretch(200,255) # really try to push out white colors
#    blobs = segmented.findBlobs() # search the image for blob objects
#    if blobs: # if blobs are found
#        circles = blobs.filter([b.isCircle(0.2) for b in blobs]) # filter out only circle shaped blobs
#        if circles:
#            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3) # draw the circle on the main image
#	    print circles[-1].meanColor()

    if normaldisplay: # if normal display mode
        only_weed.show()
    else: # segmented mode
        segmented.show()
