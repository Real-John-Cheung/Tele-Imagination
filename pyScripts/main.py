from ast import For
import imgFunctions 
import cv2
import yolo
import styleTrans
import time
import math
import random

n = styleTrans.get_model_no()
current = 1
alpha = 0
gap = 5000
dur = 2000

def mapf(x, a, b, c, d):
    return ((x-a)/(b-a)) * (d-c) + c

def get_alpha(gap_ms, duration_ms, highcut):
    if duration_ms >= gap_ms:
        raise Exception('are u nut?')
    t = time.time()
    t = math.floor(t)
    z = t % gap_ms
    if z > duration_ms: 
        global gap, dur
        if (gap - z) < 500: 
            gap = gap * random.randrange(0.8, 1.2)
            dur = dur * random.randrange(0.8, 1.2)
            while (dur >= gap):
                dur = dur * random.randrange(0.8, 1.2)
        return 0
    s = abs(math.sin(z/duration_ms))
    if s > highcut:
        return 1
    return mapf(s, 0, highcut, 0, 1)

while True:
    img = imgFunctions.getImage()
    stylized = styleTrans.predict(img)

    get_alpha(gap, dur, 0.6)

    if alpha > 0 and alpha < 1:
        merged = cv2.addWeighted(stylized, alpha, img, 1 - alpha, 0)
        imgFunctions.showImage("Main", merged)
    elif alpha == 0:
        imgFunctions.showImage("Main", img)
    elif alpha == 1:
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
        