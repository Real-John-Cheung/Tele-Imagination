import imgFunctions 
import cv2

while True:
    img = imgFunctions.getImage()
    imgFunctions.showImage("Main")
    if ord('q')==cv2.waitKey(50):
        imgFunctions.closeWindow("Main")