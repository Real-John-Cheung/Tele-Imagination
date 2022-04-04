import imgFunctions 
import cv2
import yolo

while True:
    img = imgFunctions.getImage()
    imgFunctions.showImage("Main", img)
    print(yolo.getObjects(img))
    if ord('q')==cv2.waitKey(50):
        imgFunctions.closeWindow("Main")