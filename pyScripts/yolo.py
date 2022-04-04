import cv2

with open('ml_models/coco.names', 'r') as f:
    classes = f.read().splitlines()

net = cv2.dnn.readNetFromDarknet('ml_models/yolov4-tiny.cfg', 'ml_models/yolov4-tiny.weights')

model = cv2.dnn_DetectionModel(net)

model.setInputParams(scale=1.0 / 255, size=(608, 608), swapRB=True)

def getObjects(img):
    classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)
    objList = []
    for (classId, score, box) in zip(classIds, scores, boxes):
        objList.append([classes[classIds[0]], score])
        #[["Oriange", 0.36],...]
    return objList
