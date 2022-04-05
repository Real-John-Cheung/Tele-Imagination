import imgFunctions 
import cv2
import yolo
import styleTrans

n = styleTrans.get_model_no()
current = 1

while True:
    img = imgFunctions.getImage()
    stylized = styleTrans.predict(img)
    imgFunctions.showImage("Main", stylized)
    print(yolo.getObjects(img))
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        imgFunctions.close("Main")
        break
    elif key == ord('n'):
        current = (current + 1 + n) % n
        styleTrans.load_model(current)
    elif key == ord('p'):
        current = (current - 1 + n) % n
        styleTrans.load_model(current)
        