import imgFunctions 
import cv2
import yolo
import styleTrans

n = styleTrans.get_model_no()
print(n)
styleTrans.load_model(n-2)

while True:
    img = imgFunctions.getImage()
    stylized = styleTrans.predict(img)
    imgFunctions.showImage("Main", stylized)
    print(yolo.getObjects(img))
    if ord('q')==cv2.waitKey(50):
        imgFunctions.closeWindow("Main")