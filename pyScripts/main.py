import imgFunctions 
import cv2
import yolo
import styleTrans
import time
import math
import random
import api
import numpy as np

n = styleTrans.get_model_no()
me = "A"
current = 1
alpha = 0
gap_init = 60000
dur_init = 10000
sendgap = 7000
lastSend = 0
gap = gap_init
dur = dur_init
ingap = False
green = (198, 248, 220)
white = (255, 255, 255)
tl = (40, 390)
br = (440, 640)

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

def draw_text(img, me, data):
    l = data
    if len(data) > 5:
        l = data[-5:]
    sum = 0
    top, left  = tl
    bottom, right = br
    for line in reversed(l):
        sender = line['sender']
        cont = line['content']
        font = cv2.FONT_HERSHEY_SIMPLEX 
        fontscale = 0.7
        thickness = 1
        retval, baseLine = cv2.getTextSize(cont,fontFace=font,fontScale=fontscale, thickness=thickness)
        if sender == me:
            re_b = bottom - sum 
            re_t = bottom - sum - (retval[1] + 20)
            re_r = right
            re_l = right - (retval[0] + 20)

            tr_1 = (re_r, re_b - 5)
            tr_2 = (re_r, re_b + 10)
            tr_3 = (re_r - 10, re_b - 5)
            pts = [tr_1, tr_2, tr_3]

            tx_b = bottom - sum - 10 - baseLine
            tx_l = re_l + 10
            cv2.fillPoly(img, np.array([pts]), green)
            cv2.rectangle(img, (re_l, re_t), (re_r, re_b), thickness=-1, color=green)
            cv2.putText(img, cont, (tx_l, tx_b), fontScale=fontscale, fontFace=font, thickness=thickness, color=(0,0,0) )
            sum += retval[1] + 20 + 15
        else:
            re_b = bottom - sum 
            re_t = bottom - sum - (retval[1] + 20)
            re_l = left
            re_r = re_l+(retval[0] + 20)


            tr_1 = (re_l, re_b - 5)
            tr_2 = (re_l, re_b + 10)
            tr_3 = (re_l + 10, re_b - 5)
            pts = [tr_1, tr_2, tr_3]
            
            tx_b = bottom - sum - 10 - baseLine
            tx_l = re_l + 10
            
            cv2.fillPoly(img, np.array([pts]), white)
            cv2.rectangle(img, (re_l, re_t), (re_r, re_b), thickness=-1, color=white)
            cv2.putText(img, cont, (tx_l, tx_b), fontScale=fontscale, fontFace=font, thickness=thickness, color=(0,0,0) )
            sum += retval[1] + 20 + 15

        if bottom - sum <= top:
            break


data = api.get_data()
current_time = round(time.time() * 1000.0)

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
        draw_text(merged, me, data)
        imgFunctions.showImage("Main", merged)
    elif alpha == 0:
        draw_text(img, me, data)
        imgFunctions.showImage("Main", img)
    elif alpha == 1:
        draw_text(stylized, me, data)
        imgFunctions.showImage("Main", stylized)
    
    if len(yolo.getObjects(img)) > 0 and current_time - lastSend > sendgap:
        api.write_data(me, yolo.getObjects(img)[0][0])
        data = api.get_data()
        lastSend = current_time
    # print(alpha)
    
    #update Chat
    if (current_time % 5000 < 500):
        data = api.get_data()

    current_time = round(time.time() * 1000.0)

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
        