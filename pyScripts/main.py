from numpy import dtype
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
gap_init = 60000
dur_init = 10000
gap = gap_init
dur = dur_init
ingap = False

def mapf(x, a, b, c, d):
    return ((x-a)/(b-a)) * (d-c) + c

def get_alpha(gap_ms, duration_ms, highcut, db = False):
    if duration_ms >= gap_ms:
        raise Exception('are u nut?')
    t = round(time.time() * 1000.0)
    z = t % gap_ms
    if db: 
        print(z)
    if z > duration_ms: 
        return 0
    else:
        s = abs(math.sin(mapf(z/duration_ms, 0, 1, 0, math.pi)))
        if db: 
            print(s)
        if s > highcut:
            return 1
        else:
            return mapf(s, 0, highcut, 0, 1)

def get_merged(s, o, a):
    s_h, s_w, s_a = s.shape
    o_h, o_w, o_a = o.shape
    if s_h == o_h and s_w == o_w:
        return cv2.addWeighted(s, a, o, 1-a, 0, dtype = cv2.CV_8U)
    else:
        r_o = cv2.resize(o, (s_w, s_h))
        return cv2.addWeighted(s, a, r_o, 1-a, 0, dtype = cv2.CV_8U)


while True:
    # print(get_alpha(gap, dur, 0.6))
    img = imgFunctions.getImage()
    stylized = styleTrans.predict(img)

    alpha = get_alpha(gap, dur, 0.8)
    # alpha = 1
    if (alpha > 0): ingap = True
    if (alpha == 0) and ingap: 
        ingap = False
        gap = gap_init * (random.random() * 0.4 + 0.8)
        dur = dur_init * (random.random() * 0.4 + 0.8)
        while (dur >= gap):
            dur = dur_init * (random.random() * 0.2 + 0.8)
        current = math.floor(random.random() * n)
        styleTrans.load_model(current)

    if alpha > 0 and alpha < 1:
        merged = get_merged(stylized, img, alpha)
        imgFunctions.showImage("Main", merged)
    elif alpha == 0:
        imgFunctions.showImage("Main", img)
    elif alpha == 1:
        imgFunctions.showImage("Main", stylized)
    
    if len(yolo.getObjects(img)) > 0:
        print(yolo.getObjects(img))
    # print(alpha)
    
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
        