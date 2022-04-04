import imgFunctions 
import cv2
import yolo
import styleTrans

while True:
    img = imgFunctions.getImage()
    stylized = styleTrans.predict(img)
    imgFunctions.showImage("Main", stylized)
    print(yolo.getObjects(img))
    if ord('q')==cv2.waitKey(50):
        imgFunctions.closeWindow("Main")