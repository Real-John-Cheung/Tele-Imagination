import os
import cv2

model_path = './ml_models/instance_norm/'

models = []

for f in sorted(os.listdir(model_path)): 
    if f.endswith('.t7'):
        models.append(f)

if len(models) == 0:
    raise Exception('error in loading models')

model_loaded_i = -1

print('loading init model')

model_loaded_i = 0
model_to_load = model_path + models[model_loaded_i]

net = cv2.dnn.readNetFromTorch(model_to_load)
print('loaded model: ' + model_to_load)


def get_model_no():
    return len(models)

def load_model(i):
    if i > len(models) - 1 or i < 0:
        raise Exception('invalid model index')
    else:
        model_loaded_i = i
        model_to_load = model_path + models[model_loaded_i]
        net = cv2.dnn.readNetFromTorch(model_to_load)        
        print('loaded model: ' + model_to_load)

def resize_img(img, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    h, w = img.shape[:2]

    if width is None and height is None:
        return img
    elif width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    elif height is None:
        r = width / float(w)
        dim = (width, int(h*r))

    return cv2.resize(img, dim, interpolation = inter)

def predict(img):
    orih, oriw = img.shape[:2]
    img_copy = resize_img(img, width = 600)
    h, w = img_copy.shape[:2]
    blob = cv2.dnn.blobFromImage(img_copy, 1.0, (w, h),
        (103.939, 116.779, 123.680), swapRB=False, crop=False)

    net.setInput(blob)
    out = net.forward()
    out = out.reshape((3, out.shape[2], out.shape[3]))
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.680
    out /= 255.0
    out = out.transpose(1, 2, 0)

    res = resize_img(out, width=oriw)

    return res